# env/environment.py
from typing import Tuple
from env.models import Observation, Action, Reward
from env.tasks import TASKS
from env.graders import grade_action

class EmailEnv:
    def __init__(self):
        self.current_task = None
        self.step_count = 0
        self.done = False

    def reset(self) -> Observation:
        import random
        self.current_task = random.choice(TASKS)
        self.step_count = 0
        self.done = False

        return Observation(
            email_text=self.current_task["email"],
            step_count=self.step_count
        )

    def step(self, action: Action) -> Tuple[Observation, Reward, bool, dict]:
        self.step_count += 1

        score, feedback = grade_action(self.current_task, action)

        self.done = True  # single-step episode

        reward = Reward(score=score, feedback=feedback)

        obs = Observation(
            email_text=self.current_task["email"],
            step_count=self.step_count
        )

        return obs, reward, self.done, {}

    def state(self):
        return {
            "task": self.current_task,
            "steps": self.step_count
        }