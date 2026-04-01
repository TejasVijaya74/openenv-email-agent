# env/tasks.py

TASKS = [
    # EASY
    {
        "id": "easy_1",
        "email": "I want to reset my password",
        "intent": "password_reset",
        "priority": "low"
    },

    # MEDIUM
    {
        "id": "medium_1",
        "email": "My payment failed but money was deducted",
        "intent": "payment_issue",
        "priority": "high"
    },

    # HARD
    {
        "id": "hard_1",
        "email": "I was double charged and support is not responding",
        "intent": "escalation",
        "priority": "urgent"
    }
]