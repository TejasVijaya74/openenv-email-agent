# env/graders.py

def grade_action(task, action):
    score = 0.0

    # Intent match
    if action.intent == task["intent"]:
        score += 0.4

    # Priority match
    if action.priority == task["priority"]:
        score += 0.2

    # Response quality (simple heuristic)
    if len(action.response) > 20:
        score += 0.2

    if "sorry" in action.response.lower():
        score += 0.2

    return min(score, 1.0), "Graded based on correctness"