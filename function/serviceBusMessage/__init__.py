#- Before deploying, be sure to update your requirements.txt file by running `pip freeze > requirements.txt`
#- Known issue, the python package `psycopg2` does not work directly in Azure; install `psycopg2-binary` instead to use the `psycopg2` library in Azure

#The skelton of the `__init__.py` file will consist of the following logic:

import logging
import azure.functions as func
import psycopg2
import os
from datetime import datetime
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from azure.servicebus import ServiceBusClient

def main(msg: func.ServiceBusMessage):

    notification_id = int(msg.get_body().decode('utf-8'))
    logging.info('Python ServiceBus queue trigger processed message: %s',notification_id)

    try:
        # Get connection to database
        conn = psycopg2.connect("\
            dbname='{}' \
            user='{}' \
            host='{}' \
            password='{}'".format(os.environ['dbname'], os.environ['user'], os.environ['host'], os.environ['password']))
        cur = conn.cursor()
        # Get notification message and subject from database using the notification_id
        cur.execute("SELECT message, subject FROM public.notification WHERE id = " + str(notification_id))
        notification = cur.fetchone()

        # Get attendees email and name
        cur.execute("SELECT first_name, last_name, email FROM public.attendee")
        attendees = cur.fetchall()

        from_email = os.environ['from_email']
        sendgridapikey = os.environ['sendgridapikey']

        # Loop through each attendee and send an email with a personalized subject
        for attendee in attendees:
            message = Mail(
                from_email=from_email,
                to_emails=attendee[2],
                subject='TechConf Update \'{}\' for {}'.format(notification[1], attendee[0]),
                plain_text_content=notification[0])
            sg = SendGridAPIClient(sendgridapikey)
            sg.send(message)

        # Update the notification table by setting the completed date and updating the status with the total number of attendees notified
        completed_date = datetime.utcnow()
        status = 'Notified {} attendees'.format(len(attendees))
        cur.execute("UPDATE public.notification SET status = '{}', completed_date = '{}' WHERE id = {};".format(status, completed_date, notification_id))        
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)
        conn.rollback()
    finally:
        cur.close()
        conn.close()