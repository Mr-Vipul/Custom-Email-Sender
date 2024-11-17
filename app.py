from fastapi import FastAPI
from flask import Flask, render_template, request, redirect, url_for
from email_utils import send_email_ses
from groq_integration import generate_personalized_email
from google_sheets import get_data_from_sheets
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file.filename.endswith('.csv'):
        # Handle CSV file
        pass
    return redirect(url_for('index'))

@app.route('/send_emails', methods=['POST'])
def send_emails():
    email_data = request.form.get('email_data')
    prompt = request.form.get('prompt')
    personalized_email = generate_personalized_email(prompt)
    send_email_ses(email_data['email'], 'Personalized Subject', personalized_email)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
