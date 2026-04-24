#→ Message understanding logic
import re

def parse_message(msg: str):
    msg = msg.lower().strip()

    # Extract amount
    amount_match = re.search(r'\d+', msg)
    if not amount_match:
        return None

    amount = int(amount_match.group())

    # Remove amount from text
    desc = re.sub(r'\d+', '', msg).strip()

    # Clean symbols
    desc = desc.replace("₹", "").replace("rs", "").strip()

    if not desc:
        desc = "General"

    return {
        "amount": amount,
        "desc": desc
    }
# 🔍 What it handles:
# 500 lunch
# spent 200 on cab
# ₹300 groceries