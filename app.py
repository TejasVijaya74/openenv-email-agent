from fastapi import FastAPI
from env.environment import EmailEnv
from env.models import Action

app = FastAPI()
env = EmailEnv()

@app.get("/")
def home():
    return {"status": "running"}

@app.get("/reset")
def reset():
    obs = env.reset()
    return obs.dict()

@app.post("/step")
def step(action: dict):
    global env

    # Auto-reset if no task loaded
    if env.current_task is None:
        env.reset()

    action_obj = Action(**action)
    obs, reward, done, _ = env.step(action_obj)

    return {
        "observation": obs.dict(),
        "reward": reward.dict(),
        "done": done
    }