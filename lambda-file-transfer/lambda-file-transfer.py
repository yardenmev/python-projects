import boto3
from botocore.exceptions import ClientError
from email import message_from_bytes
import logging

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    source_bucket = 'testing-reciving-mails-admin'
    destination_bucket = 'testing-moving-email-from-reciving'

    # Get the file information from the event
    records = event['Records']
    for record in records:
        # Get the source file information
        s3 = record['s3']
        object_key = s3['object']['key']

        # Download the email from the source bucket
        s3_client = boto3.client('s3')
        try:
            response = s3_client.get_object(Bucket=source_bucket, Key=object_key)
            email_content = response['Body'].read()

            # Parse the email content
            msg = message_from_bytes(email_content)

            # Find the file attachments
            for part in msg.walk():
                if part.get_content_maintype() == 'multipart':  # Skip multipart emails
                    continue
                if part.get('Content-Disposition') is None:  # Skip attachments without disposition
                    continue

                # Extract the file content from the attachment
                file_content = part.get_payload(decode=True)

                # Extract the filename from the attachment
                filename = part.get_filename()

                if not filename:
                    continue  # Skip if filename is missing

                logger.info(f"Found attachment: {filename}")

                # Upload the file to the destination bucket
                s3_client.put_object(Body=file_content, Bucket=destination_bucket, Key=filename)

                logger.info(f"Moved attachment to destination bucket: {filename}")

            # Delete the email from the source bucket
            s3_client.delete_object(Bucket=source_bucket, Key=object_key)
            logger.info("Deleted email from source bucket.")

        except ClientError as e:
            logger.error(e.response['Error']['Message'])
