import streamlit as st
import os
from langchain.memory import ConversationBufferMemory
from utils import get_chat_response

st.title("💭ChatRobot")
openai_api_key=os.getenv("OPENAI_API_KEY")
if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    st.session_state["messages"] = [{"role": "ai", "content": "我是你的AI助手，有什么可以帮你的吗？"}]

# 显示聊天记录，只需要维护messages列表
for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input("给AI发送消息")
if prompt:
    if not openai_api_key:
        st.info("请设置OpenAI_API_Key环境变量！")
        st.stop()
    # 新增用户消息
    st.session_state["messages"].append({"role": "human", "content": prompt})
    st.chat_message("human").write(prompt)
    with st.spinner("AI思考中..."):
        # AI回答
        response = get_chat_response(prompt, st.session_state["memory"], openai_api_key)
        st.session_state["messages"].append({"role": "ai", "content": response})
        st.chat_message("ai").write(response)
if st.button("清除对话历史"):
    # 清空会话记录，重置memory和messages
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    st.session_state["messages"] = [{"role": "ai", "content": "我是你的AI助手，有什么可以帮你的吗？"}]