import streamlit as st
from model_service import ModelService

############################################
# LLM Response Generation and Chat
############################################

st.subheader("Chat with your AI Assistant, Sen's Giang!")
if "model_service" not in st.session_state:
    st.session_state["model_service"] = ModelService()

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Can you tell me what you need?")

if user_input:
    st.session_state["messages"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        augmented_user_input = st.session_state["model_service"].get_relevant_vectorstore(user_input)
        for response in st.session_state["model_service"].chain.stream({"input": augmented_user_input}):
            full_response += response
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
        st.session_state["model_service"].update_prompt_template(user_input, full_response)
    st.session_state["messages"].append({"role": "assistant", "content": full_response})
