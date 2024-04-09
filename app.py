import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

## Function to get LLama2 response.
def getLLamaresponse(input_text,no_words,text_style):
    ### LLama model
    llm=CTransformers(model='/Users/jayanthkoripalli/Downloads/llama-2-7b-chat.ggmlv3.q8_0.bin',
                      model_type= 'llama',
                      config={'max_new_tokens':256,
                              'temperature':0.01})
    template=f"""
    Write a paragraph for {text_style} for a topic {input_text} within {no_words} words, weather how safe is it to travel alone or at night at that location"""
    prompt=PromptTemplate(input_variables=["style","text",'n_words'],
                          template=template)
    response=llm(prompt.format(style=text_style,text=input_text,n_words=no_words))
    print(response)
    return response


    st.set_page_config(page_title="Crime Analysis using Llama 2",
                   layout='centered',
                   initial_sidebar_state='collapsed')
st.header("Crime Analysis")
input_text=st.text_input("Enter the place and time you want to analyze")
col1, col2= st.columns([5,5])
with col1:
    no_words=st.text_input("No of words")
with col2:
    text_style= st.selectbox('Generating the analysis for',('Research','Educational','Safety'), index=0)
submit=st.button("Generate")
## Final Response

if submit:
    st.write(getLLamaresponse(input_text,no_words,text_style))