from langchain.agents import Tool
import streamlit as st

def create_appointment_tool():
    def tool_fn(input_text):
        st.session_state["start_form"] = True
        return "Let's start collecting your appointment information."

    return Tool(
        name="AppointmentForm",
        func=tool_fn,
        description="Use this when a user wants to book a call or appointment."
    )
