# ⚡ OrderFlow - Serverless Order Management System

![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)

## 🌐 Project Status & Source Code

> 💡 **Note for Reviewers & Hiring Managers:**
> This project was successfully deployed as a live cloud application using **AWS Amplify** and an asynchronous serverless backend. 
> 
> **Original Deployment URL:** `https://staging.dlgeznd717vj3.amplifyapp.com`
> 
>
> You can fully explore the production-ready code structure directly within this repository:

---

## Overview
[cite_start]OrderFlow is a fully serverless, event-driven order management platform built as a cloud-native architecture[cite: 1, 28]. [cite_start]It demonstrates a decoupled system design where a lightweight JavaScript web client interacts with a highly scalable, asynchronous AWS backend[cite: 26, 28].

## Key Features
- [cite_start]**Event-Driven Architecture**: Asynchronous processes orchestrated via **AWS Step Functions** to decouple operations[cite: 26, 28].
- [cite_start]**Parallel Processing**: Order deletion triggers **SNS** email notifications to subscribers and backs up deleted records to **S3** simultaneously without blocking the main workflow threads[cite: 26, 33].
- [cite_start]**RESTful APIs**: Robust endpoints driving CRUD operations using **API Gateway & Lambda**, with persistent storage in **DynamoDB**[cite: 30, 31, 32].
- [cite_start]**Automated Reporting**: Generates on-demand PDF summaries of all deleted orders from S3 via a dedicated Lambda function[cite: 34, 42].
- [cite_start]**AI Integration**: Leverages **AWS Rekognition** to analyze uploaded product images and auto-fill order descriptions based on machine-learning detected labels[cite: 35, 46].

## Tech Stack
* [cite_start]**Frontend:** JavaScript (ES6+), HTML5, CSS3 (Configured for AWS Amplify) [cite: 35]
* [cite_start]**Backend & Compute:** Python, AWS Lambda, Amazon API Gateway [cite: 30, 31, 34]
* [cite_start]**Database & Storage:** Amazon DynamoDB (NoSQL), Amazon S3 [cite: 32, 34]
* [cite_start]**Orchestration & Messaging:** AWS Step Functions, Amazon SNS [cite: 33]
* [cite_start]**AI / Machine Learning:** Amazon Rekognition [cite: 35]

## System Architecture & Flow
1. [cite_start]**Client requests** are routed securely via **API Gateway** to dedicated **Lambda** microservices[cite: 37, 38].
2. [cite_start]**State management** and fast querying are handled via **DynamoDB** partition keys[cite: 39, 46].
3. [cite_start]**Asynchronous execution** handles heavy tasks (archiving and third-party notifications) in parallel via **Step Functions**, ensuring immediate API responses and a smooth, unblocked user experience[cite: 26, 40, 41].
