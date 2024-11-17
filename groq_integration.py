import groq

def generate_personalized_email(prompt):
    """Generate personalized email using Groq API"""
    client = groq.Client(api_key="your_groq_Api")
    response = client.query(prompt)
    return response.get("text", "")
