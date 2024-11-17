import groq

def generate_personalized_email(prompt):
    """Generate personalized email using Groq API"""
    client = groq.Client(api_key="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")
    response = client.query(prompt)
    return response.get("text", "")
