from pydantic import BaseModel, Field

class CalculatorInput(BaseModel):
    question: str = Field()
