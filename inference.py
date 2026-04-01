import os
from openai import OpenAI
from env.environment import EmailEnv
from env.models import Action

client = OpenAI(
    base_url=os.getenv("API_BASE_URL"),
    api_key=os.getenv("HF_TOKEN")
)

MODEL = os.getenv("MODEL_NAME")

env = EmailEnv()

def run_episode():
    obs = env.reset()

    prompt = f"""
    Email:
    {obs.email_text}

    Classify intent, priority and write response.
    Output JSON:
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    text = response.choices[0].message.content

    import json
    data = json.loads(text)

    action = Action(**data)

    _, reward, _, _ = env.step(action)

    return reward.score

if __name__ == "__main__":
    scores = [run_episode() for _ in range(5)]
    print("Average Score:", sum(scores)/len(scores))