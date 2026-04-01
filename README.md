---
title: OpenEnv Email Agent
emoji: 📧
colorFrom: blue
colorTo: green
sdk: docker
app_file: app.py
pinned: false
---
# OpenEnv Email Triage Environment

Real-world OpenEnv environment for email triage.

## Tasks

This environment includes multiple levels of difficulty:

- **Easy**: Password reset, account updates  
- **Medium**: Payment failures, billing issues  
- **Hard**: Escalations, refund requests with urgency  

## Reward Design

The reward function evaluates:

- Intent correctness (40%)
- Priority correctness (20%)
- Response quality (length, tone, empathy)
- Special handling (refund/escalation cases)

Partial rewards are given to guide agent learning.

## Use Case

This environment simulates real-world customer support workflows and can be used to train AI agents for:

- Email triage automation  
- Customer support assistance  
- LLM evaluation benchmarking  

