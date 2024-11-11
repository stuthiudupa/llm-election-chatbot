"""
This example is to show Chain Of Thought
"""

from langchain import PromptTemplate
from load_llm import load_llm

template = """Answer the question based on the context below. If the
question cannot be answered using the information provided answer
with "I don't know".

Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. Each can contains 3 tennis balls. How many 
tennis balls does he have now?
A: Roger started with 5 balls. 2 cans of 3 tennis balls is 6 tennis balls. 5+6 = 11.The answer is 11.

Q: The cafetaria has 23 apples. If they used 20 apples for lunch and bought 6 more, how many apples do they have?

"""


prompt_template = PromptTemplate(
    input_variables=[],
    template=template
)

prompt = prompt_template.format(
    )

llm = load_llm()
print(llm(prompt))
