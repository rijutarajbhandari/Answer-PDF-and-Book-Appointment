from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain

def get_conversational_chain():
    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""
        Answer the question using the provided context.
        If the answer is not present, say: "answer is not available in the context".
        
        Context:
        {context}
        
        Question:
        {question}
        """
    )
    model = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', temperature=0.5)
    return load_qa_chain(model, chain_type="stuff", prompt=prompt)
