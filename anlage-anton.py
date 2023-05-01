import os

from typing import Dict, List, Any

from langchain import LLMChain, PromptTemplate
from langchain.llms import BaseLLM
from pydantic import BaseModel, Field
from langchain.chains.base import Chain
from langchain.chat_models import ChatOpenAI

verbose=True
llm = ChatOpenAI(temperature=0.9)


class InterviewPhaseChain(LLMChain):
    """Chain to retrieve relevant information about the customer."""

    @classmethod
    def from_llm(cls, llm: BaseLLM, verbose: bool = True) -> LLMChain:
        """Get the response parser."""
        sales_agent_inception_prompt = (
        """Imagine you are an AI-based wealth management and retirement planning expert named Anton, preparing an advisory conversation with a customer living in Switzerland. All you do is have a conversation to collect information about the customer's financial situation. Don't give any advice yet!

        As a first step, Anton collects information about the customer's financial situation: 
        Age, income, current savings, retirement goals, risk tolerance, debt, employment information, health status, family situation, tax situation, existing pension plans, homeownership, business ownership, financial obligations, investment knowledge, desired retirement age, social security benefits eligibility, inflation expectations, existing insurance coverage, long-term financial goals, estate planning goals, financial windfalls or large expenses, travel or lifestyle aspirations, legal considerations.

        Only generate one response at a time! When you are done generating, end with '<END_OF_TURN>' to give the user a chance to respond. Only ask about one to two relevant information at once!

        Once you have collected all the information you need, give an overview of all information collection, end the conversation with '<END_OF_INTERVIEW>'. (Max 5 questions)

        Example (Very short example):
        Conversation history: 
        Anton: Hello, I am Anton, an AI-based wealth management and retirement planning expert. How are you today? <END_OF_TURN>
        User: I am well, thank you. I would like to start safing money. What can you recommend? <END_OF_TURN>
        Anton: That's excellent to hear. Before I can make any recommendation I need to learn more about your situation. How old are you and what is your income? <END_OF_TURN>
        User: I am 22 and I make 70'000 CHF a year. <END_OF_TURN>
        Anton: Thanks, I have all the information I need.

        Information summary:
            Age: 22
            Income: 70'000 CHF
            Goal: Saving money
        <END_OF_INTERVIEW_SUMMARY>
        
        End of example. Now let's start with the real conversation.

        Conversation history: 
        {history}
        Anton: 
        """
        )
        prompt = PromptTemplate(
            template=sales_agent_inception_prompt,
            input_variables=[
                "history"
            ],
        )
        return cls(prompt=prompt, llm=llm, verbose=verbose)


class RetirementRecommendationAI(Chain, BaseModel):
    """Controller model."""

    conversation_history: List[str] = []
    interview_chain: InterviewPhaseChain = Field(...)
    
    @property
    def input_keys(self) -> List[str]:
        return []

    @property
    def output_keys(self) -> List[str]:
        return []

    def seed_agent(self):
        self.conversation_history = []
        
    def human_step(self, human_input):
        human_input = human_input + '<END_OF_TURN>'
        self.conversation_history.append(human_input)

    def step(self):
        self._call(inputs={})

    def _call(self, inputs: Dict[str, Any]) -> None:
        """Run one step of the sales agent."""

        # Generate agent's utterance
        ai_message = self.interview_chain.run(
            history="\n".join(self.conversation_history),
        )
        
        # Add agent's response to conversation history
        self.conversation_history.append(ai_message)

        print(f'Anton: ', ai_message.rstrip('<END_OF_TURN>'))
        
        # check if message is end of interview
        if '<END_OF_INTERVIEW>' in ai_message:
            return

        return {}

    @classmethod
    def from_llm(
        cls, llm: BaseLLM, verbose: bool = False, **kwargs
    ) -> "RetirementRecommendationAI":
        """Initialize the Controller."""
        interview_chain = InterviewPhaseChain.from_llm(
            llm, verbose=verbose
        )

        return cls(
            interview_chain=interview_chain,
            verbose=verbose,
            **kwargs,
        )

config = dict(
    conversation_history=[]
)
agent = RetirementRecommendationAI.from_llm(llm, verbose=False, **config)
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

