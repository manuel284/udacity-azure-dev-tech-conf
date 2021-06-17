# TechConf Registration Website

## Project Overview
The TechConf website allows attendees to register for an upcoming conference. Administrators can also view the list of attendees and notify all attendees via a personalized email message.

## Monthly Cost Analysis
### For this project:

For this project, I chose the most cost efficient or even free service tiers.

| Azure Resource | Service Tier | Monthly Cost |
| ------------ | ------------ | ------------ |
| *Azure Postgres Database* | Basic, 1 vCore(s), 5 GB | $29.65 |
| *Azure Service Bus* | Basic | < $0.01|
| *Web App* | F1 | $0.00 |
| *Function App* | F1 | $.0.00 |
| *SendGrid*   | Free |  $0.00|
| *Storage Account*   | Storage (general purpose v1) | < $0.01|
| __Total__                   |         | ~$29.67 |

### In a production environment:

| Azure Resource | Service Tier | Monthly Cost |
| ------------ | ------------ | ------------ |
| *Azure Postgres Database* | Basic, 1 vCore(s), 5 GB | $29.65 |
| *Azure Service Bus* | Basic | < $0.01|
| *Web App* | Basic Tier; 1 B1 (1 Core(s), 1.75 GB RAM, 10 GB Storage) x 730 Hours; Linux OS | $13.14|
| *Function App* | Basic Tier; 1 B1 (1 Core(s), 1.75 GB RAM, 10 GB Storage) x 730 Hours; Linux OS | $13.14 |
| *SendGrid*   | Bronze; 40,000 e-mails/month; | $9.95|
| *Storage Account*   | Storage (general purpose v1) | < $0.01|
| __Total__                   |         | ~$65.90 |

For the Azure Service Bus, I assumed 10,000 messaging operations.

## Architecture Explanation
For this application, we are using an Azure Postgres Database to store the data.
The web site runs on an Azure App Service. It is connected to the dabase and also sends messages to an Azure Service Bus Queue.
An Azure Function reads messages from that queue, sends out e-mails via SendGrid and updates a table in the postgreSQL db.

The application was monolithic before the migration. Notifications were sent out synchronously which caused HTTP timeout exceptions.
It was maybe still running on old hardware which is neither scalable nor cost-effective. 

Azure allows us to scale all of the resources we are using if needed. So, we are able to increase or decrease our resources based on the current or future load. This is also very cost-effective because we don't have to buy hardware. Instead we just scale up/out our resources if we need to handle more load. And when the load decreses we can scale down/in again.

The web app now sends a message to the Azure Service Bus Queue whenever a notification gets created. So the user creating the notification immediately gets an http response and doesn't have to wait for the notifications to be sent. The Azure Function App then pulls that message and sends out e-mail notifications to all attendees.


In a production environment, we cannot use the free tiers for our function/web app and SendGrid.
I would start with the basic postgreSQL db and then scale if necessary.
I would also start with the basic tier for the service bus. It supports queues and a message size 256 KB. That's all we need in the beginning.
For the web and function app, I would also start with the basic tier and scale if needed.
The bronze tier of SendGrid allows us to send 40,000 e-mails a month. If many people register for the conference and/or we send out many notifications, the tier needs to be upgraded.
