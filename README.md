# AnlageAnton - AI-based Wealth Management

AnlageAnton is an AI-based wealth management solution using GPT-4 to provide optimal retirement plans for users. It utilizes a conversational AI interface to gather information and provide recommendations.

## Features

- Interview-based information retrieval
- Retirement plan recommendations
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

export AZURE_DEPLOYMENT_NAME=<your_azure_deployment_name>
export AZURE_MODEL_NAME=<your_azure_model_name>
export OPENAI_API_TYPE=azure
export OPENAI_API_VERSION=2023-03-15-preview
export OPENAI_API_BASE=https://<your-azure-service>.openai.azure.com/
export OPENAI_API_KEY=<your-key>

2. Make sure to replace `<your_azure_deployment_name>` and `<your_azure_model_name>` with your actual Azure Chat OpenAI deployment and model names.

## Usage

1. Run the main.py script:
```python main.py```

2. Follow the prompts and interact with the AI to provide the necessary information and receive your optimal retirement plan.
