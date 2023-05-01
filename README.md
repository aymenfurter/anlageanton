# AnlageAnton - AI-based Wealth Management - Sample App

AnlageAnton is an AI-based wealth management solution using GPT-4 to provide optimal retirement plans for users. It utilizes a conversational AI interface to gather information and provide recommendations.

## Features

- Interview-style information retrieval (inspired by [SalesGPT](https://python.langchain.com/en/latest/use_cases/agents/sales_agent_with_context.html))
- Retirement plan recommendations (based on a [Custom LLM Agent](https://python.langchain.com/en/latest/modules/agents/agents/custom_llm_chat_agent.html#)
- Integration with Azure Chat OpenAI

## Prerequisites

- Python 3.8 or higher
- Azure Chat OpenAI account

## Installation

1. Clone the repository: 
```
git clone https://github.com/yourusername/AnlageAnton.git
```

2. Change to the project directory:
```
cd AnlageAnton
```

3. Install the required packages:
```pip install -r requirements.txt```

## Configuration

1. Set up environment variables:
```
export AZURE_DEPLOYMENT_NAME=<your_azure_deployment_name>
export AZURE_MODEL_NAME=<your_azure_model_name>
export OPENAI_API_TYPE=azure
export OPENAI_API_VERSION=2023-03-15-preview
export OPENAI_API_BASE=https://<your-azure-service>.openai.azure.com/
export OPENAI_API_KEY=<your-key>
```
2. Make sure to replace `<your_azure_deployment_name>` and `<your_azure_model_name>` with your actual Azure Chat OpenAI deployment and model names.

## Usage

1. Run the main.py script:
```python main.py```

2. Follow the prompts and interact with the AI to provide the necessary information and receive your optimal retirement plan.

## Sample run
This follow sample run showcases a conversation between AnlageAnton and a user. Anton demonstrates the following features:
- The AI collects relevant information about the user, such as age, income, risk tolerance, debt, family situation, homeownership status, pension plans, and healthcare costs, to provide personalized advice.
- Anton effectively summarizes the user's information to confirm its accuracy, ensuring a tailored retirement plan.
- After gathering the necessary information, Anton's internal "Thought" process analyzes Urs's situation and generates an optimal retirement plan.
- The AI expert provides Urs with a personalized retirement plan with valuable action points such as making voluntary AHV contributions for the spouse

<img src="https://raw.githubusercontent.com/aymenfurter/anlageanton/main/example-run.png?token=GHSAT0AAAAAACBEWPS6BA4TQCBK4YXB7FC6ZCQALNQ">
