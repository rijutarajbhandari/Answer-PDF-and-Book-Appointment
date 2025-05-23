import streamlit as st
from utils.pdf_utils import get_pdf_text, get_pdf_tables
from utils.validation import parse_date_from_text
from vectorstore.vector_utils import get_text_chunks, get_vector_store
from chains.qa_chain import get_conversational_chain
from utils.form_utils import collect_user_info
from agents.appointment_tool import create_appointment_tool
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType
from dotenv import load_dotenv
import os

load_dotenv()
st.set_page_config(page_title="Answer PDF and Book Appointment")
genai_api_key = os.getenv("GOOGLE_API_KEY")

def user_input(user_question):
    if "call me" in user_question.lower() or "book" in user_question.lower():
        tool = create_appointment_tool()
        agent = initialize_agent(
            tools=[tool],
            llm=ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', temperature=0.5),
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=False,
        )
        agent.run(user_question)
        return

    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    docs = db.similarity_search(user_question)

    chain = get_conversational_chain()
    response = chain({"input_documents": docs, "question": user_question}, return_only_outputs=True)
    st.write("Reply: ", response.get("output_text", "No response generated."))

def main():
    st.header("Answer PDF and Book Appointment")

    if st.session_state.get("start_form"):
        info = collect_user_info()
        if info:
            st.write(f"✅ Appointment booked for {info['name']} on {info['date']}")
            st.session_state["start_form"] = False

    user_question = st.chat_input("Ask a Question from the PDF Files")
    if user_question:
        user_input(user_question)

    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF Files", accept_multiple_files=True, type=["pdf"])
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                table_text = get_pdf_tables(pdf_docs)
                full_text = raw_text + "\n" + table_text
                chunks = get_text_chunks(full_text)
                get_vector_store(chunks)
                st.success("Processing complete!")

if __name__ == "__main__":
    if "start_form" not in st.session_state:
        st.session_state["start_form"] = False
    main()
