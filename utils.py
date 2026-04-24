#→ Helpers (formatting, validation)
def format_currency(amount):
    return f"₹{amount}"

def format_summary(month, total):
    return f"📊 Total for {month}: ₹{total}"

def error_message():
    return "❌ Invalid input. Try: 500 lunch"