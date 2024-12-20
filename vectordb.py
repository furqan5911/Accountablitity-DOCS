
import os
from dotenv import load_dotenv
import openai
from pinecone import Pinecone, ServerlessSpec
import streamlit as st



OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

# Initialize Pinecone and OpenAI

# Define the Pinecone index and namespace
INDEX_NAME= 'ams'
NAMESPACE = 'docs-ams'

# Initialize Pinecone instance
pc = Pinecone(api_key=PINECONE_API_KEY)
# create the index
if INDEX_NAME not in pc.list_indexes().names():
    pc.create_index(
        name=INDEX_NAME,
        dimension=1536,  # dimensionality of dense model
        metric="cosine",  # sparse values supported only for dotproduct
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )
index = pc.Index(INDEX_NAME)
openai.api_key = OPENAI_API_KEY


def generate_embedding(text):
    response = openai.embeddings.create(
        input=text,
        model="text-embedding-ada-002"  # Ensure this matches your model choice
    )
    return response.data[0].embedding

def query_pinecone(query, top_k=5):
    # Generate embedding for the user query
    query_embedding = generate_embedding(query)
    
    # Query Pinecone index
    result = index.query(
        vector=query_embedding,
        top_k=top_k,
        namespace=NAMESPACE,
        include_metadata=True
    )
    
    return result


def main():
    st.set_page_config(page_title="Chat with your file")
    st.header("Accountablitity DOCS")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    with st.sidebar:
        openai_api_key = st.text_input("OpenAI API Key", type="password")
        if openai_api_key:
            openai.api_key = openai_api_key
        else:
            st.warning("Please enter your OpenAI API key.")
            st.stop()

    user_question = st.text_input("Ask a question about your documents:")
    if user_question:
        with st.spinner("Retrieving relevant information..."):
            search_results = query_pinecone(user_question)
            st.session_state.chat_history.append(("User", user_question))
            if search_results and 'matches' in search_results:
                # Iterate over the matches to find the first available content
                for match in search_results['matches']:
                    metadata = match.get('metadata', {})
                    # Check for 'content' key; if absent, check for 'text' key
                    answer = metadata.get('content') or metadata.get('text')
                    if answer:
                        st.session_state.chat_history.append(("Bot", answer))
                        break
                else:
                    # If no content or text found in any match
                    st.session_state.chat_history.append(("Bot", "No relevant information found."))
            else:
                st.session_state.chat_history.append(("Bot", "No relevant information found."))


    if st.session_state.chat_history:
        for speaker, message in st.session_state.chat_history:
            if speaker == "User":
                st.markdown(f"**You:** {message}")
            else:
                st.markdown(f"**DocumentGPT:** {message}")

if __name__ == '__main__':
    main()
