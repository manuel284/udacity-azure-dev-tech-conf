## Screenshots

The following screenshots should be taken and uploaded to this **screenshots** folder:

1. **Migrate Web Applications - 2 Screenshots**
 - Screenshot of Azure Resource showing the **App Service Plan**.
  - Screenshot of the deployed Web App running. The screenshot should be fullscreen showing the URL and application running.
  ![web app service plan](screenshots/1-1b.png)
  ![web app overview](screenshots/1-1.png)
  Live URL: https://app-toast-techconf.azurewebsites.net/
  ![web app live](screenshots/1-2.png)
2. **Migrate Database - 2 Screenshots**
 - Screenshot of the Azure Resource showing the **Azure Database for PostgreSQL server**.
 ![sql overview](screenshots/2-1.png)
 - Screenshot of the Web App successfully loading the list of **attendees** and **notifications** from the deployed website.
 ![sql overview](screenshots/2-2.png)
3. **Migrate Background Process - 4 Screenshots**
 - Screenshot of the Azure Function App running in Azure, showing the **function name** and the **function app plan**.
 ![function app service plan](screenshots/3-1b.png)
 ![function app overview](screenshots/3-1.png)
 ![function app function](screenshots/3-1c.png)
 - Screenshots of the following showing functionality of the deployed site:
    
    For this step, I deleted the existing rows from the attendees table and registered two new attendees with my own e-mail addresses.
    ![web app new user1](screenshots/3-0.png)
    ![web app new user2](screenshots/3-0b.png)
    1. Submitting a new notification.
      - Screenshot of filled out **Send Notification** form.
      ![web app notifiaction](screenshots/3-2.png)
    2. Notification processed after executing the Azure function.
      - Screenshot of the **Email Notifications List** showing the notification status as **Notifications submitted**.
      ![web app notifiaction submitted](screenshots/3-3.png)
      - Screenshot of the **Email Notifications List** showing the notification status as **Notified X attendees**.
      ![web app notifiaction notified](screenshots/3-4.png)
      ![web app notifiaction receive1](screenshots/3-4b.png)
      ![web app notifiaction receive2](screenshots/3-4c.png)
