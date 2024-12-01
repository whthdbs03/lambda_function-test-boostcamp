# README.md

# Lambda Function Deployment Guide

This guide provides instructions on setting up a virtual environment, installing necessary packages, configuring environment variables, and uploading your AWS Lambda function.

## Project Structure

```
├── README.md
├── lambda_function.py
├── upload_lambda_function.py
├── requirements.txt
├── .env
└── .gitignore
```

## Setup Instructions

### 1. Create a Virtual Environment

Create and activate a virtual environment to manage project dependencies.

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

### 2. Install Required Packages

Install the necessary Python packages.

```bash
pip install boto3 python-dotenv
```

### 3. Save Dependencies

Freeze the installed packages into a `requirements.txt` file.

```bash
pip freeze > requirements.txt
```

Alternatively, install packages from an existing `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root directory and add your AWS credentials and configuration.

```plaintext
AWS_ACCESS_KEY=YOUR_ACCESS_KEY
AWS_SECRET_KEY=YOUR_SECRET_KEY
AWS_REGION=YOUR_REGION
LAMBDA_FUNCTION_NAME=YOUR_LAMBDA_FUNCTION_NAME
```

**Note:** Replace `YOUR_ACCESS_KEY`, `YOUR_SECRET_KEY`, `YOUR_REGION`, and `YOUR_LAMBDA_FUNCTION_NAME` with your actual AWS credentials and Lambda function name.

### 5. Upload the Lambda Function

Run the upload script to deploy your Lambda function.

```bash
python upload_lambda_function.py
```

## Now you're all set!

You can now set up the virtual environment, install the necessary packages, and easily update your Lambda function.