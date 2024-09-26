import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import HumanMessage, SystemMessage
from langchain import PromptTemplate, LLMChain

# Set your Hugging Face API token directly
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

# openai.api_key = 'sk-M1tQzbLFW_XMBTPe56iQBJM_q-CYkeJZhG-wSYlZwhT3BlbkFJsHxCPN2S8HbM2kUiZarXD1FcsndCPMnKl8ZqYWSOkA'


# Create the LLM endpoint
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    max_new_tokens=512,
    do_sample=False,
    repetition_penalty=1.03,
)

chat_model = ChatHuggingFace(llm=llm)

messages = [
    SystemMessage(content="You're a helpful assistant"),
    HumanMessage(content="Why the plants color is green?"),
]

# try:
#     # Invoke the model
#     ai_msg = chat_model.invoke(messages);    
#     print(" Response ", ai_msg.content)
# except Exception as e:
#     print(e)


# question = "What is generative ai?"
# template = """Question = {question}
# Answer = Let's think step by step."""
# prompt = PromptTemplate(template=template, input_variables=["question"])
# llm_chain = LLMChain(llm = llm, prompt=prompt)
# print(llm_chain.invoke(question)['text'])


# If using the downloaded model use HuggingFacePipeline
from langchain_huggingface import HuggingFacePipeline
from transformers import AutoModelForCasualLM, Autotokenizer, pipeline

model_selected = "gpt-2"
llm_model = AutoModelForCasualLM.from_pretrained(model_selected)
tokenizer = Autotokenizer.from_pretrained(model_selected)

pipeline = pipeline("text-generation", model = llm_model, tokenizer=tokenizer, max_new_tokens=100)
model_hf = HuggingFacePipeline(pipeline = pipeline)
print(model_hf.invoke("Tesla is a company "))
