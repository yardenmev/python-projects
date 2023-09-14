# AWS Lambda Email Attachment Processor



An AWS Lambda function that processes incoming emails with attachments, extracts the attachments, and moves them to another S3 bucket.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Description

The AWS Lambda Email Attachment Processor is designed to work as an AWS Lambda function that listens to incoming emails in an S3 bucket. It detects emails with attachments, extracts the attachments, and moves them to a different S3 bucket. This automation can be useful for processing email attachments in a serverless manner.

## Features

- Monitors an S3 bucket for incoming emails.
- Automatically extracts email attachments.
- Moves the extracted attachments to another S3 bucket.
- Customizable and extendable for specific use cases.

## Usage

To use this AWS Lambda function, follow these steps:

1. Create an S3 bucket to receive incoming emails (e.g., `testing-reciving-mails-admin`).
2. Create an S3 bucket to store the extracted attachments (e.g., `testing-moving-email-from-reciving`).

### AWS Lambda Configuration

3. Create an AWS Lambda function using the AWS Lambda console.
4. Set up an S3 trigger for the Lambda function, specifying the source bucket (`testing-reciving-mails-admin`) as the event source.
5. Deploy the Lambda function with the provided script (`lambda_function.py`).

### S3 Bucket Configuration

6. Grant appropriate permissions to the Lambda function to read from the source bucket (`testing-reciving-mails-admin`) and write to the destination bucket (`testing-moving-email-from-reciving`).

Now, whenever an email with attachments is uploaded to the source bucket, the Lambda function will automatically process it.

## Configuration

You may need to modify the Lambda function script (`lambda_function.py`) to fit your specific requirements:

- Update the `source_bucket` and `destination_bucket` variables with your S3 bucket names.
- Customize the logging level and format in the script as needed.

## Contributing

Contributions to this project are welcome! If you have improvements, bug fixes, or new features to propose, please follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes and test them thoroughly.
4. Commit your changes and push to your fork.
5. Submit a pull request with a detailed description of your changes.


