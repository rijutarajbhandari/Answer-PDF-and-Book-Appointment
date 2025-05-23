# Answer-PDF-and-Book-Appointment
This is a Streamlit-based application that allows users to upload PDF files, ask questions based on the document content, and optionally book an appointment using a conversational form powered by LangChain and Gemini (Google Generative AI).

 ## Features

- 📄 Upload multiple PDFs and extract both text and tables
- 🧠 Embedding with Google Generative AI + FAISS vector store
- 💬 Ask natural language questions about the uploaded documents
- 📅 Conversational appointment form:
  - Name, Phone Number, Email
  - Smart date parsing (e.g., “in 3 days” → `YYYY-MM-DD`)
  - Input validation (email, phone)
- 🔌 Tool-agent integration for dynamic form completion

  ## Tech Stack

- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [Gemini (Google Generative AI)](https://makersuite.google.com/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [PyPDF2](https://github.com/py-pdf/PyPDF2)
- [dateparser](https://github.com/scrapinghub/dateparser)
- [Tabula-py](https://github.com/chezou/tabula-py)

## Installation
git clone https://github.com/rijutarajbhandari/Answer-PDF-and-Book-Appointment.git
cd chat-with-pdf


## Install dependencies
pip install -r requirements.txt

## Setup Environment Variables
Create a .env file in the root directory and add your Google API Key:
GOOGLE_API_KEY=your_google_api_key_here

## Running the App
streamlit run app.py

## How to Use
- Upload PDFs
   - Go to the sidebar
   - Click “Upload your PDF Files”
   - Select one or more PDFs and click Submit & Process
   -Text and tables are extracted and vectorized automatically
- Ask Questions
- Book an Appointment
  - Ask: “Schedule an appointment" or "Book an appointment in 3 days"
  - Fill the form
  - The chatbot confirms the extracted information






