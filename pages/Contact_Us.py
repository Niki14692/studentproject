import streamlit as st
from send_email import send_email
import pandas

# create header
st.header("Contact Us")

# create dataframe
df = pandas.read_csv("topic.csv")

# prepare email form
with st.form(key="email_forms"):
    user_email = st.text_input("Your Email Address")
    option = st.selectbox('What topic do you want to discuss?', df["topic"])
    a_message = st.text_area("Text")
    message = f"""\
Subject: New email from {user_email}
    
{user_email}
Topic {option}
{a_message}
"""
    submit = st.form_submit_button("Submit")
    if submit:
        send_email(message)
        st.info("Your email was sent successfully.")

