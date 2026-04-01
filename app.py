from fastapi import FastAPI, HTTPException
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


@app.get("/state")
def state():
    return env.state()


@app.post("/step")
def step(action: Action):
    try:
        # Ensure environment initialized
        if env.current_task is None:
            raise HTTPException(
                status_code=400,
                detail="Environment not initialized. Call /reset first."
            )

        obs, reward, done, _ = env.step(action)

        return {
            "observation": obs.dict(),
            "reward": reward.dict(),
            "done": done
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))