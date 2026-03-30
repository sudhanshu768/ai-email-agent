def preprocess_email(email_text: str) -> str:
    # Basic cleaning (you can improve later)
    email_text = email_text.strip()
    email_text = email_text.replace("\n", " ")
    return email_text