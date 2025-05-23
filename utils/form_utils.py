import streamlit as st
from utils.validation import is_valid_email, is_valid_phone, parse_date_from_text

def collect_user_info():
    st.subheader("📋 Book an Appointment")
    with st.form(key="user_info_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone Number (e.g., +1234567890)")
        date_text = st.text_input("Preferred Date (e.g., in 3 days)")

        submitted = st.form_submit_button("Submit")
        if submitted:
            if not name or not is_valid_email(email) or not is_valid_phone(phone):
                st.error("Invalid name, email or phone number.")
                return None

            parsed_date = parse_date_from_text(date_text)
            if not parsed_date:
                st.error("Could not parse the date.")
                return None

            return {"name": name, "email": email, "phone": phone, "date": parsed_date}
    return None
