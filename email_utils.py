import boto3
from botocore.exceptions import NoCredentialsError

def send_email_ses(to_email, subject, body):
    """Send email using Amazon SES"""
    try:
        client = boto3.client(
            'ses',
            aws_access_key_id='YOUR_AWS_ACCESS_KEY_ID',
            aws_secret_access_key='YOUR_AWS_SECRET_ACCESS_KEY',
            region_name='YOUR_AWS_REGION'
        )
        response = client.send_email(
            Source='your-email@example.com',
            Destination={'ToAddresses': [to_email]},
            Message={
                'Subject': {'Data': subject},
                'Body': {'Text': {'Data': body}}
            }
        )
        return response
    except NoCredentialsError:
        print("Credentials not available.")
        return None
