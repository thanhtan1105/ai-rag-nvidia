# 🤖 AI Assistant Application - Using RAG and LLM in NVIDIA 🚀

Welcome to the future! This application is a chatbot named "Sen's Giang" built with Python and Streamlit. It uses a language model to generate responses based on user input and context from uploaded documents. The application leverages NVIDIA's RAG (Retrieval Augmented Generation) and LLM (Language Language Model) for response generation. It's like having your own personal Jarvis! 🦾

## 📁 Files

- `main.py`: This is the main application file. It handles the Streamlit interface and manages the chat functionality. It's like the brain of our operation! 🧠

- `model_service.py`: This file contains the `ModelService` class which handles the language model and document embeddings. It also manages the knowledge base built from uploaded documents. It's the heart of our AI assistant! ❤️

- `build_knowledge.py`: This script is used to build the knowledge base from uploaded documents. It's like feeding our AI assistant with knowledge! 📚

## 🚀 Usage

1. Upload your PDF files to the `uploaded_docs` folder. These documents will be used to build the knowledge base for our AI assistant. It's like giving our AI assistant a good read! 📖

2. Run `build_knowledge.py` to build the knowledge base from the uploaded documents. It's like feeding our AI assistant with knowledge! 🍔

3. Run `main.py` to start the Streamlit application. Let's get this party started! 🎉

4. Interact with the chatbot through the Streamlit interface. Have fun chatting! 💬

## 🧩 Applying RAG and LLM in NVIDIA

The `ModelService` class in `model_service.py` is responsible for applying RAG and LLM in NVIDIA. It uses the `ChatNVIDIA` class for the LLM and the `NVIDIAEmbeddings` class for the document embeddings. The `build_knowledge` method is used to build the knowledge base from uploaded documents, which is then used by the `get_relevant_vectorstore` method to retrieve relevant documents based on the user input. The `update_prompt_template` method is used to update the prompt template based on the user input and the generated response. It's like magic, but with code! 🎩✨

## 📚 Dependencies

- Python 🐍
- Streamlit 🌟
- langchain_core 🧬
- langchain_text_splitter ✂️
- langchain_vectorstores 🗃️
- langchain_nvidia_ai_endpoints 🎯
- cloudpickle 🥒
- pdf_loader 📄

Please ensure these dependencies are installed before running the application. It's like making sure you have all the ingredients before baking a cake! 🍰

## 📝 Note

This application is designed to respond based on the context provided. If a question is out of context, the AI assistant will refrain from replying and politely decline to respond to the user. It's like teaching our AI assistant manners! 🎩

## References

https://github.com/NVIDIA/GenerativeAIExamples

https://www.youtube.com/watch?v=N_OOfkEWcOk