import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from embedding import vectordb
from langchain.prompts import PromptTemplate
from constants import *
from templates import prompt_template

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
llm = ChatGroq(
    temperature=0.9,
    groq_api_key=groq_api_key,
    model_name=LLM)

prompt = PromptTemplate(
    input_variables=["chat_history", "context", "question"],
    template=prompt_template,
)

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=vectordb.as_retriever(search_kwargs={"k": 3}),
    memory=memory,
    combine_docs_chain_kwargs={"prompt": prompt},

)

while True:
    query = input("\n❓ Ask something about Your Resume (or 'exit' to quit): ")
    if query.lower() == "exit":
        break
    result = qa_chain.invoke({"question": query})
    print("\n💬 Answer:", result["answer"])
