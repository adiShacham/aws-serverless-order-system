# ⚡ OrderFlow - Serverless Order Management System

![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)

## Overview
OrderFlow is a fully serverless, event-driven order management platform. It features a responsive web client communicating with a robust backend built entirely on AWS cloud-native services. 

## Key Features
- **Event-Driven Architecture**: Asynchronous processes orchestrated via **AWS Step Functions**.
- **Parallel Processing**: Order deletion triggers **SNS** email notifications to subscribers and backs up deleted records to **S3** simultaneously without blocking the UI.
- **RESTful APIs**: Robust endpoints driving CRUD operations using **API Gateway & Lambda**, stored in **DynamoDB**.
- **Automated Reporting**: Generates on-demand PDF summaries of all deleted orders.
- **AI Integration**: Leverages **AWS Rekognition** to analyze uploaded product images and auto-fill order descriptions based on machine-learning detected labels.

## Tech Stack
* **Frontend:** JavaScript (ES6+), HTML5, CSS3, Hosted on AWS Amplify
* **Backend & Compute:** Python, AWS Lambda, Amazon API Gateway
* **Database & Storage:** Amazon DynamoDB (NoSQL), Amazon S3
* **Orchestration & Messaging:** AWS Step Functions, Amazon SNS
* **AI / Machine Learning:** Amazon Rekognition
