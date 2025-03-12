import streamlit as st
import requests

# API base URL
API_BASE_URL = "https://escalyticsv7api.onrender.com"

st.title("Email Analysis Application")

# Function to analyze email
def analyze_email(email_content, selected_scenario):
    url = f"{API_BASE_URL}/analyze_email"
    payload = {
        "email_content": email_content,
        "selected_scenario": selected_scenario
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

# Function to analyze attachment
def analyze_attachment(file):
    url = f"{API_BASE_URL}/analyze_attachment"
    files = {"file": file}
    response = requests.post(url, files=files)
    return response.json()

# Function to analyze email attachment
def analyze_email_attachment(file):
    url = f"{API_BASE_URL}/analyze_email_attachment"
    files = {"file": file}
    response = requests.post(url, files=files)
    return response.json()

# Tab selection
tab = st.sidebar.radio("Select Tab", ["Analyze Email", "Analyze Attachment", "Analyze Email Attachment"])

if tab == "Analyze Email":
    st.header("Analyze Email")
    email_content = st.text_area("Email Content")
    selected_scenario = st.text_input("Selected Scenario")
    
    if st.button("Analyze Email"):
        if email_content:
            result = analyze_email(email_content, selected_scenario)
            st.json(result)
        else:
            st.error("Please enter the email content.")

elif tab == "Analyze Attachment":
    st.header("Analyze Attachment")
    uploaded_file = st.file_uploader("Choose a file", type=["txt", "pdf", "docx", "eml", "xlsx"])
    
    if st.button("Analyze Attachment"):
        if uploaded_file:
            result = analyze_attachment(uploaded_file)
            st.json(result)
        else:
            st.error("Please upload a file.")

elif tab == "Analyze Email Attachment":
    st.header("Analyze Email Attachment")
    uploaded_file = st.file_uploader("Choose an email file", type=["eml", "msg"])
    
    if st.button("Analyze Email Attachment"):
        if uploaded_file:
            result = analyze_email_attachment(uploaded_file)
            st.json(result)
        else:
            st.error("Please upload an email file.")
