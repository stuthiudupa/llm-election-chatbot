import streamlit as st
from get_completion_client import get_completion

# from llm_client import do_llm
# from load_llm import get_llm

st.markdown(f'## Super Neta: Gen AI powered Politics')
st.write(
    """
    ##### This demo illustrates Prompt Engineering techniques!!
"""
)

# llm = get_llm()
prompt = st.chat_input(placeholder="Your message")
if prompt:
    st.write("Your prompt is: " + prompt)
    # response = llm(prompt)
    response = get_completion(prompt)
    print(response)
    st.write("Agent: " + str(response))
