def grade_action(task, action):
    score = 0.0

    valid_intents = [
        "password_reset",
        "account_update",
        "payment_issue",
        "billing_issue",
        "escalation",
        "refund_request"
    ]

    # Intent match
    if action.intent == task["intent"]:
        score += 0.4
    elif action.intent in valid_intents:
        score += 0.2
    else:
        score -= 0.2  # penalty

    # Priority match
    if action.priority == task["priority"]:
        score += 0.2

    # Response quality
    response = action.response.lower()

    if len(response) > 20:
        score += 0.1

    if "sorry" in response or "apolog" in response:
        score += 0.1

    if "refund" in response and task["intent"] == "refund_request":
        score += 0.2

    # Clamp score
    score = max(0.0, min(score, 1.0))

    return score, "Graded based on correctness and quality"