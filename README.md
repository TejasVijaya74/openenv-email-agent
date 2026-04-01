\---

title: OpenEnv Email Agent

emoji: 📧

colorFrom: blue

colorTo: green

sdk: docker

app\_file: app.py

pinned: false

\---



\# OpenEnv Email Triage Environment



This project implements a real-world OpenEnv environment for customer support email triage.



\## Features



\- Email classification (intent detection)

\- Priority assignment

\- Automated response generation

\- Reward-based grading system

\- FastAPI-based environment endpoints



\## API Endpoints



\- `/reset` → Initialize environment

\- `/step` → Take action and receive reward

\- `/state` → Get current environment state



\## Tech Stack



\- Python

\- FastAPI

\- OpenEnv Core

\- Docker



\## Usage



Run locally:



```bash

uvicorn app:app --reload

