from flask import Flask, render_template, request, jsonify
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os
import pandas as pd
from langchain_core.documents import Document
from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings
from langchain_astradb import AstraDBVectorStore
from langchain_groq import ChatGroq
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import create_history_aware_retriever
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

load_dotenv()
ASTRA_DB_API_ENDPOINT = os.getenv("ASTRA_DB_API_ENDPOINT")
ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_KEYSPACE = os.getenv("ASTRA_DB_KEYSPACE")
HF_TOKEN = os.getenv("HF_TOKEN")
GROQ_API = os.getenv("GROQ_API")

app = Flask(__name__)

def extract_info(soup):
    return [
        {
            'title': eachHead.find("h3", {"class": "dataset-heading"}).find('a').text,
            'link': eachHead.find("h3", {"class": "dataset-heading"}).find('a').attrs['href'],
            'datasetOrganiz': eachHead.find("div", {"class": "notes"}).find('p', {"class": "dataset-organization"}).text,
            'description': eachHead.find("div", {"class": "notes"}).find('div').text,
        } for eachHead in soup.find_all("div", {"class": "dataset-content"})
    ]

url_list = ["https://catalog.data.gov/dataset?res_format=XML"]
final_doc = []
for eachPage in url_list:
    r = requests.get(eachPage)
    soup = BeautifulSoup(r.content, 'html.parser')
    final_doc += extract_info(soup)

df = pd.DataFrame(final_doc)

docs = [Document(page_content=obj['description'], metadata={'title': obj['title']}) for obj in final_doc]

embeddings = HuggingFaceInferenceAPIEmbeddings(api_key=HF_TOKEN, model_name="BAAI/bge-base-en-v1.5")
vstore = AstraDBVectorStore(
    embedding=embeddings,
    collection_name="datasetAggregator",
    api_endpoint=ASTRA_DB_API_ENDPOINT,
    token=ASTRA_DB_APPLICATION_TOKEN,
    namespace=ASTRA_DB_KEYSPACE
)
vstore.add_documents(docs)

model = ChatGroq(groq_api_key=GROQ_API, model="llama-3.1-70b-versatile", temperature=0.5)
retriever_prompt = ("Given a chat history and the latest user question which might reference context in the chat history, "
                    "formulate a standalone question which can be understood without the chat history. "
                    "Do NOT answer the question, just reformulate it if needed and otherwise return it as is.")
retriever = vstore.as_retriever(search_kwargs={"k": 3})
contextualize_q_prompt = ChatPromptTemplate.from_messages(
    [("system", retriever_prompt), MessagesPlaceholder(variable_name="chat_history"), ("human", "{input}")]
)
history_aware_retriever = create_history_aware_retriever(model, retriever, contextualize_q_prompt)

DATASET_BOT_TEMPLATE = """
    You are an expert bot for providing insights about datasets.
    Your role is to analyze dataset titles and descriptions to help users find relevant information and answer their queries accurately.
    Ensure your responses are concise, informative, and remain focused on the context of the dataset.
    Avoid providing irrelevant or off-topic information.

    CONTEXT:
    {context}

    QUESTION: {input}

    YOUR ANSWER:
"""
qa_prompt = ChatPromptTemplate.from_messages(
    [("system", DATASET_BOT_TEMPLATE), MessagesPlaceholder(variable_name="chat_history"), ("human", "{input}")]
)

question_answer_chain = create_stuff_documents_chain(model, qa_prompt)
chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)

store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

chain_with_memory = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history",
    output_messages_key="answer",
)

@app.route('/')
def index():
    return render_template('index.html') 
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['input'] 
    session_id = 'default_session'
    response = chain_with_memory.invoke(
        {"input": user_input},
        config={"configurable": {"session_id": session_id}},
    )["answer"]
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
