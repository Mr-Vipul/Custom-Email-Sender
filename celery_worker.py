from celery import Celery
from email_utils import send_email_ses
from groq_integration import generate_personalized_email

celery = Celery('email_task', broker='redis://localhost:6379/0')

@celery.task
def send_email_task(email_data, prompt):
    personalized_email = generate_personalized_email(prompt)
    send_email_ses(email_data['email'], 'Personalized Subject', personalized_email)
