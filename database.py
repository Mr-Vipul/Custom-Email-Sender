import sqlite3

DATABASE = 'emails.db'

def init_db():
    """Initialize SQLite database and create table"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS emails (id INTEGER PRIMARY KEY, email TEXT, status TEXT)''')
    conn.commit()
    conn.close()

def save_email_status(email, status):
    """Save email status to the database"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO emails (email, status) VALUES (?, ?)', (email, status))
    conn.commit()
    conn.close()

def get_email_status():
    """Retrieve all email statuses"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM emails')
    rows = cursor.fetchall()
    conn.close()
    return rows
