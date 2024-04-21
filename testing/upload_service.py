from app.model_service import ModelService
import cloudpickle as pickle

model_service = ModelService()
with open(model_service.vector_store_path, "rb") as f:
    vectorstore = pickle.load(f)

user_input = 'List all table of contents of a Book?'

retriever = vectorstore.as_retriever()
docs = retriever.get_relevant_documents(user_input)

context = ""
for doc in docs:
    context += doc.page_content + "\n\n"

augmented_user_input = "Context: " + context + "\n\nQuestion: " + user_input + "\n"

full_response = ""
for response in model_service.chain.stream({"input": augmented_user_input}):
    full_response += response

print(full_response)