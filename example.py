def analyze_email(email):

    if "refund" in email:
        intent = "Refund Request"
    elif "late" in email or "delay" in email:
        intent = "Delivery Issue"
    else:
        intent = "General Complaint"

    if "angry" in email or "frustrated" in email:
        emotion = "Negative"
    else:
        emotion = "Neutral"

    return intent, emotion


email = "My order is late and I'm frustrated"

intent, emotion = analyze_email(email)

print("Intent:", intent)
print("Emotion:", emotion)
