#Entry point (API + WhatsApp webhook)
from fastapi import FastAPI, Request
from parser import parse_message
from sheets import add_expense, get_summary
from utils import format_currency, format_summary, error_message

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/webhook")
async def whatsapp_webhook(request: Request):
    data = await request.form()

    msg = data.get("Body", "")
    user = data.get("From", "")

    try:
        msg_lower = msg.lower()

        # 📊 Summary
        if "show" in msg_lower:
            month = msg_lower.replace("show", "").strip().title()

            total, _ = get_summary(month)

            return {
                "message": format_summary(month, total)
            }

        # ➕ Add expense
        parsed = parse_message(msg)

        if not parsed:
            return {"message": error_message()}

        add_expense(parsed["amount"], parsed["desc"], user)

        return {
            "message": f"✅ Added {format_currency(parsed['amount'])} for {parsed['desc']}"
        }

    except Exception as e:
        return {"message": "⚠️ Something went wrong"}