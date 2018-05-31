![DBG](images/dbg-horizontal.png)

# Cloud Infrastructure - NAME

Offering Managers: Jane Doe (Business Unit)

Development: Jane Doe (Engineer)

Month Day, Year

![DBG](images/dbg-vertical.png)

&nbsp;
&nbsp;
&nbsp;
&nbsp;

## Overview

Enhance existing messaging systems with simple transformations to create new processes and data transformations with the least amount of code using Apache OpenWhisk.

## Architecture Diagram

![Architecture](images/architecture.png)

## IBM Products

* Message Hub
* OpenWhisk

## Related Technologies

* Apache Kafka

## Key Features

Serverless computing, message processing with Apache Kafka, minimal code
techniques.

## Rationale

This introduction to OpenWhisk enables developers on the simplest way to add new Cloud functions to existing systems. It demonstrates the zero-infrastructure and minimal code techniques to create whole new business flows that tie into an existing messaging system. OpenWhisk is an amazing value to developers only using 1 line of code. 

## Code Pattern Hypothesis

### Opportunity

* This Code Pattern targets developers learning serverless and low code techniques and IBM Cloud users looking to leverage event based integration

### Operational Efficiency

* Demonstrates the power of one line of code with minimal configuration to add new capabilities to solutions

* Highlights developer productivity – zero server admin, rapid application cycles

### Community and Advocacy

* Cloud native communities and enterprise development communities where message oriented middleware patterns can be shown in the Cloud native form
* DevOps conferences with rapid apps focus

### Amplification

* Expand to show other event triggers in the Bluemix platform – simple document management over storage
* Mobile app versions with push/simple notification integration
* Consider Swift community demos showing rapid business logic/backend changes * Would consider a more data oriented example (such as events on weather forecast changes, IoT sensors, etc)

### Competition

* AWS Lambda has the most mature offering in the market with event triggers broadly supported in the AWS platform
* No other vendor has an open serverless platform, emphasize integrations with 3rd parties wherever possible to highlight OpenWhisk community

## Concept

### What is the Code Pattern?

This project shows the power of serverless, event-driven architectures to execute code in response to messages or to handle streams of data records.

The application demonstrates two OpenWhisk actions (written in JavaScript) that read and write messages with IBM Message Hub (based on Apache Kafka). The use case demonstrates how actions can work with data services and execute logic in response to message events.

One action receives message streams of one or more data records. These records are piped to another action in an OpenWhisk sequence (a way to link actions declaratively in a chain). The second action aggregates the message and posts a transformed summary message to another topic.

### Who is it for?

This Code Pattern targets developers learning serverless and low code techniques and IBM Cloud users looking to leverage event based integration.

### What will they learn?

Serverless demonstrates the power of one line of code with minimal configuration to add new capabilities to solutions. This Code Pattern highlights the benefits of using this technology for developer productivity – zero server
admins required, rapid application cycles, etc. With very little effort, a developer can now add event driven responses to messages to extend an existing application.

## What does it look like?

1. Provision Message Hub
2. Create OpenWhisk actions, triggers, and rules
3. Test new message events
4. Delete actions, triggers, and rules
5. Recreate deployment manually

# Strategy

## What is the strategy?

Serverless computing, also known as function as a service (FaaS), is a cloud computing code execution model in which the cloud provider fully manages starting and stopping of a function's container platform as a service (PaaS)
as necessary to serve requests, and requests are billed by an abstract measure of the resources required to satisfy the request, rather than per virtual machine, per hour.

Despite the name, it does not actually involve running code without servers. The name "serverless computing" is used because the business or person that owns the system does not have to purchase, rent or provision servers or virtual machines for the back-end code to run on.

In many of today’s cloud-native applications, data is generated at huge volumes and is used to link highly distributed services. Apache Kafka provides a system to stream messages at scale, but the systems that receive those messages must be able to process and act on individual records as well.

With an event-driven architecture built on OpenWhisk (IBM’s open serverless technology), you can write functions that respond to messages from queues and execute logic to process or send data to other systems in a distributed architecture. And you’ll pay only for the resources consumed by your analytics functions for the fractions of a second that they run. This gives you a tight match between transactions processed and cloud resources used.

This is the promise of an event-driven, serverless architecture for new cloud-native applications such as those that support high volume stream-based message processing.

AWS Lambda has the most mature offering in the market with event triggers broadly supported in the AWS platform. AWS Kinesis is a cloud-based managed alternative to Kafka, which is directly competitive to IBM’s Bluemix Message Hub. Many existing tutorials exist for processing large data streams with event driven serverless technology on AWS:

* http://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html
* http://docs.aws.amazon.com/lambda/latest/dg/with-kinesis-example.html
* https://aws.amazon.com/blogs/big-data/persist-streaming-data-to-amazon-s3-using-amazon-kinesis-firehose-and-aws-lambda/
* https://hackernoon.com/processing-real-time-big-data-streams-using-kinesis-lambda-561a029ef305

Despite this clear advantage, no other vendor has an open serverless platform, emphasize integrations with 3rd parties wherever possible than the IBM OpenWhisk community. It is an immediate opportunity for IBM to highlight our Open by Design strategy in a space where we are behind our competition with documentation for developers looking to on-ramp into using serverless technologies.

## What is the advocacy potential?

This Code Pattern is relevant to cloud native, serverless, and enterprise development communities where message oriented patterns can be shown in the Cloud native form.

## What are some target events or meetups?

DevOps, Serverless, and Open Source meetups and conferences with rapid app development focus:

* DevOps Days (many worldwide)
* Container Camp AU (5/22-24)
* Cloud Expo NYC (6/6)
* OSCON (5/10)
* OSCON EU (11/6)
* Open Source Summit LA (9/11-13)
* Open Source Summit Tokyo (5/31)
* Open Source Summit Europe (10/23)
* CloudNativeCon / KubeCon Austin (12/6)
* ApacheCon North America (5/16)
* Serverless Conf (4/26)
* Serverless Conf Europe (10/24)
* Kafka Summit SF (8/28)

## How does this impact the city and community Heat Maps?

This Code Pattern is an opportunity to advocate in Cloud Native and Serverless communities, where IBM is sorely behind the competition - OpenWhisk is a critical for competing with Amazon Lambda in all cities.

## What are the key metrics for this Code Pattern?

1. \# Github repo forks
2. \# Deploys to Bluemix
3. \# Readme page views
4. % reduction in churn from monthly active users (MAU) versus non-Code Pattern MAU

