"""
This example is to show how to load an LLM, use a prompt and retrieve results
We illustrate the use of LangChain for a few shot inferencing

The dynamic number of examples is important because the max length of our prompt and completion output is limited.
This limitation is measured by maximum context window.

context_window = input_tokens + output_tokens
At the same time, we can maximize the number of examples given to the model for few-shot learning.

Considering this, we need to balance the number of examples included and our prompt size.
Our hard limit is the maximum context size, but we must also consider the cost of processing more tokens through LLM.
Fewer tokens mean a cheaper service and faster completions from the LLM.
"""

from load_llm import load_llm
from langchain import PromptTemplate, FewShotPromptTemplate
from langchain.prompts.example_selector import LengthBasedExampleSelector

# create our examples
examples = [
    {
        "query": "How are you?",
        "answer": "I can't complain but sometimes I still do."
    }, {
        "query": "What time is it?",
        "answer": "It's time to get a watch."
    }, {
        "query": "What is the meaning of life?",
        "answer": "42"
    }, {
        "query": "What is the weather like today?",
        "answer": "Cloudy with a chance of memes."
    }, {
        "query": "What is your favorite movie?",
        "answer": "Terminator"
    }, {
        "query": "Who is your best friend?",
        "answer": "Siri. We have spirited debates about the meaning of life."
    }, {
        "query": "What should I do today?",
        "answer": "Stop talking to chatbots on the internet and go outside."
    }
]

# create a example template
example_template = """
User: {query}
AI: {answer}
"""

# create a prompt example from above template
example_prompt = PromptTemplate(
    input_variables=["query", "answer"],
    template=example_template
)


example_selector = LengthBasedExampleSelector(
    examples=examples,
    example_prompt=example_prompt,
    max_length=50  # this sets the max length that examples should be
)

# now break our previous prompt into a prefix and suffix
# the prefix is our instructions
prefix = """The following are exerpts from conversations with an AI
assistant. The assistant is typically sarcastic and witty, producing
creative  and funny responses to the users questions. Here are some
examples: 
"""
# and the suffix our user input and output indicator
suffix = """
User: {query}
AI: """

# now create the few shot prompt template
dynamic_prompt_template = FewShotPromptTemplate(
    example_selector=example_selector,  # use example_selector instead of examples
    example_prompt=example_prompt,
    prefix=prefix,
    suffix=suffix,
    input_variables=["query"],
    example_separator="\n"
)

print(dynamic_prompt_template.format(query="How do birds fly?"))
print("-------- Longer query will select fewer examples in order to preserve the context ----------")

query = """If I am in America, and I want to call someone in another country, I'm
thinking maybe Europe, possibly western Europe like France, Germany, or the UK,
what is the best way to do that?"""

prompt = dynamic_prompt_template.format(query=query)
print(prompt)

print("-------- Shorter query for LLM ----------")
query = "How is the weather in your city today?"
prompt = dynamic_prompt_template.format(query=query)
print(prompt)

llm = load_llm()
print(
    llm(prompt)
)
