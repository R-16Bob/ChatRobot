import os

from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain

from langchain.memory import ConversationBufferMemory

def get_chat_response(prompt, memory, openai_api_key):
    model = ChatOpenAI(model="gpt-4o-mini", openai_api_key=openai_api_key, base_url="https://api.aigc369.com/v1")
    chain = ConversationChain(llm=model, memory=memory)

    response = chain.invoke({"input": prompt})
    return response["response"]

if __name__ == "__main__":
    openai_api_key=os.getenv("OPENAI_API_KEY")
    model = ChatOpenAI(model="gpt-4o-mini", openai_api_key=openai_api_key, base_url="https://api.aigc369.com/v1")
    memory = ConversationBufferMemory(return_messages=True)
    print(get_chat_response("牛顿提出过哪些著名的定律？", memory, openai_api_key ))