from app.services.gemini_service import classify_intent
def intent_node(state: dict) -> dict:
    email = state.get("email", "")

    intent = classify_intent(email)

    return {
        **state,
        "intent": intent
    }