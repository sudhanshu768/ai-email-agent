from fastapi import FastAPI
from app.graph.email_graph import build_graph
from app.services.gmail_service import get_emails
from app.utils.preprocess import preprocess_email

app = FastAPI()

graph = build_graph()

@app.get("/")
def root():
    return {"message": "Server is working ✅"}

@app.get("/process-emails")
def process_emails():
    emails = get_emails()

    results = []

    for email in emails:
        clean_email = preprocess_email(email)

        output = graph.invoke({
            "email": clean_email
            })

        print("DEBUG:", output)  # 👈 ADD THIS

        results.append(output if output else {"error": "No output"})

    return {"results": results}