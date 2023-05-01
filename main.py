import os
from config import load_configuration
from retirement_recommendation_ai import RetirementRecommendationAI

config = load_configuration()
agent = RetirementRecommendationAI.from_llm(**config)
agent.seed_agent()

while True:
    agent.step()

    human_input = input("You: ")
    if human_input.lower() == "exit":
        break

    agent.human_step(human_input)
    if human_input.lower() == "exit":
        break
    agent.human_step(human_input)
