from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain_nvidia_ai_endpoints import ChatNVIDIA, NVIDIAEmbeddings
import os
import cloudpickle as pickle
from pdf_loader import PDFLoader


class ModelService:
    def __init__(self):
        self.llm = ChatNVIDIA(model="mixtral_8x7b", max_tokens=1024)
        self.document_embedder = NVIDIAEmbeddings(model="nvolveqa_40k",
                                             model_type="passage")
        self.user_input_prompt = ("user", "{input}")
        self.prompt_template = ChatPromptTemplate.from_messages(
            [("system", "You are a helpful AI assistant named Sen's Giang. You will reply to questions only based on the context that you are provided. If something is out of context, you will refrain from replying and politely decline to respond to the user."),
             self.user_input_prompt
             ]
        )

        self.chain = self.prompt_template | self.llm | StrOutputParser()
        self.vector_store_path = "./app/vectorstore.pkl"
        self.DOCS_DIR = os.path.abspath("./uploaded_docs")

    def build_knowledge(self):
        files = os.listdir(self.DOCS_DIR)
        for file in files:
            raw_documents = PDFLoader.extract_text_from_pdf(self.DOCS_DIR + "/" + file)
            text_splitter = CharacterTextSplitter()
            documents = text_splitter.create_documents(text_splitter.split_text(raw_documents))
            vectorstore = FAISS.from_documents(documents, self.document_embedder)
            with open(self.vector_store_path, "wb") as f:
                pickle.dump(vectorstore, f)

    def get_relevant_vectorstore(self, user_input):
        with open(self.vector_store_path, "rb") as f:
            vectorstore = pickle.load(f)
            retriever = vectorstore.as_retriever()
        docs = retriever.get_relevant_documents(user_input)
        context = ""
        for doc in docs:
            context += doc.page_content + "\n\n"

        # append content
        return "Context: " + context + "\n\nQuestion: " + user_input + "\n"

    def update_prompt_template(self, user_input, full_response):
        new_prompt = self.prompt_template.messages.copy()
        new_prompt[-1] = ChatPromptTemplate.from_messages([("user", user_input)]).messages[0]
        new_prompt.append(ChatPromptTemplate.from_messages([("assistant", full_response)]).messages[0])
        new_prompt.append(ChatPromptTemplate.from_messages([self.user_input_prompt]).messages[0])
        self.prompt_template = ChatPromptTemplate.from_messages(new_prompt)
        print(self.prompt_template.messages)
