# ⚡ OrderFlow - Serverless Order Management System

![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)

> 💡 **Note for Reviewers:**
> This project was successfully deployed as a live cloud application using **AWS Amplify** and an asynchronous serverless backend. 
> 
> **Original Deployment URL:** `https://staging.dlgeznd7l7vj3.amplifyapp.com/`
> 
> You can fully explore the production-ready code structure directly within this repository:

---
## Overview
OrderFlow is a fully serverless, event-driven order management platform built as a cloud-native architecture. It demonstrates a decoupled system design where a lightweight JavaScript web client interacts with a highly scalable, asynchronous AWS backend.

## Key Features
- **Event-Driven Architecture**: Asynchronous processes orchestrated via **AWS Step Functions** to decouple operations.
- **Parallel Processing**: Order deletion triggers **SNS** email notifications to subscribers and backs up deleted records to **S3** simultaneously without blocking the main workflow threads.
- **RESTful APIs**: Robust endpoints driving CRUD operations using **API Gateway & Lambda**, with persistent storage in **DynamoDB**.
- **Automated Reporting**: Generates on-demand PDF summaries of all deleted orders.
- **AI Integration**: Leverages **AWS Rekognition** to analyze uploaded product images and auto-fill order descriptions based on machine-learning detected labels.

## Tech Stack
* **Frontend:** JavaScript (ES6+), HTML5, CSS3, (Configured for AWS Amplify)
* **Backend & Compute:** Python, AWS Lambda, Amazon API Gateway
* **Database & Storage:** Amazon DynamoDB (NoSQL), Amazon S3
* **Orchestration & Messaging:** AWS Step Functions, Amazon SNS
* **AI / Machine Learning:** Amazon Rekognition

## System Architecture & Flow
1. **Client requests** are routed securely via **API Gateway** to dedicated **Lambda** microservices.
2. **State management** and fast querying are handled via **DynamoDB** partition keys.
3. **Asynchronous execution** handles heavy tasks (archiving and third-party notifications) in parallel, ensuring immediate API responses and a smooth, unblocked user experience.
