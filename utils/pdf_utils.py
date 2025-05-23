from PyPDF2 import PdfReader
import tabula
import streamlit as st

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        reader = PdfReader(pdf)
        for page in reader.pages:
            text += page.extract_text()
    return text

def get_pdf_tables(pdf_docs):
    table_text = ""
    for pdf in pdf_docs:
        try:
            tables = tabula.read_pdf(pdf, pages="all", multiple_tables=True, silent=True, pandas_options={"header": None})
            for table in tables:
                table_text += table.to_string(index=False) + "\n"
        except Exception as e:
            st.warning(f"Could not extract tables from {pdf.name}: {e}")
    return table_text
