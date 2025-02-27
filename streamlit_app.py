import streamlit as st
import requests

# The URL of the FastAPI service
API_URL = "https://escalyticsv6api.onrender.com/analyze"

# Features to analyze, you can change this to suit your needs
FEATURES = {
    "Sentiment": "sentiment",
    "Highlights": "highlights",
    "Response": "response",
    "Tone": "tone",
    "Task Extraction": "task_extraction",
    "Subject Recommendation": "subject_recommendation",
    "Clarity": "clarity",
    "Complexity Reduction": "complexity_reduction",
    "Phishing Detection": "phishing_detection",
    "Sensitive Info Detection": "sensitive_info_detection",
    "Confidentiality Rating": "confidentiality_rating",
    "Attachment Analysis": "attachment_analysis"
}

# Streamlit UI
st.title("Email Analysis with AI")

# File upload
uploaded_file = st.file_uploader("Upload Email/Text File", type=["txt", "pdf", "docx", "eml"])

# Email content input box
email_content = st.text_area("Or, paste your email content here:")

# Scenario selection (dropdown)
scenarios = ["General", "Urgent", "Formal", "Casual"]
selected_scenario = st.selectbox("Select email scenario", scenarios)

# Feature selection (checkboxes)
selected_features = {}
for feature_name, feature_key in FEATURES.items():
    selected_features[feature_key] = st.checkbox(feature_name, value=True)

# Submit button
if st.button("Analyze"):
    if not email_content and not uploaded_file:
        st.error("Please provide email content or upload an email file.")
    else:
        # Prepare the request payload
        request_payload = {
            "email_content": email_content,
            "selected_scenario": selected_scenario,
            "features": selected_features
        }

        files = {}
        if uploaded_file:
            files = {"uploaded_file": uploaded_file}

        # Send the POST request to the FastAPI backend
        headers = {"accept": "application/json"}
        
        # To handle both text and file upload together, you need to send JSON for text and a file in the multipart format
        if uploaded_file:
            # For the file upload, we need to use the multipart form data (which `requests` can handle automatically)
            response = requests.post(API_URL, headers=headers, json=request_payload, files=files)
        else:
            # For the text case, just send the JSON payload
            response = requests.post(API_URL, headers=headers, json=request_payload)

        # Check if the response is successful
        if response.status_code == 200:
            analysis_results = response.json()

            # Display the analysis results
            st.subheader("Analysis Results")
            if analysis_results.get("error"):
                st.error(analysis_results["error"])
            else:
                for feature, result in analysis_results.items():
                    if result:
                        st.write(f"**{feature.replace('_', ' ').title()}:** {result}")
                    else:
                        st.write(f"**{feature.replace('_', ' ').title()}:** No data")
        else:
            st.error(f"Error: {response.status_code}, {response.text}")
