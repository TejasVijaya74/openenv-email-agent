TASKS = [
    # EASY
    {
        "id": "easy_1",
        "email": "I want to reset my password",
        "intent": "password_reset",
        "priority": "low"
    },
    {
        "id": "easy_2",
        "email": "How can I change my email address?",
        "intent": "account_update",
        "priority": "low"
    },

    # MEDIUM
    {
        "id": "medium_1",
        "email": "My payment failed but money was deducted",
        "intent": "payment_issue",
        "priority": "high"
    },
    {
        "id": "medium_2",
        "email": "I was charged twice for my subscription",
        "intent": "billing_issue",
        "priority": "high"
    },

    # HARD
    {
        "id": "hard_1",
        "email": "I was double charged and support is not responding",
        "intent": "escalation",
        "priority": "urgent"
    },
    {
        "id": "hard_2",
        "email": "This is unacceptable. I want a refund immediately or I will file a complaint.",
        "intent": "refund_request",
        "priority": "urgent"
    }
]