import streamlit as st
import requests

# The URL of the FastAPI service
BASE_API_URL = "https://escalyticsv6api.onrender.com"

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
            "scenario": selected_scenario,
            "features": selected_features
        }

        # Prepare the multipart/form-data request
        files = {}
        if uploaded_file:
            files = {"file": uploaded_file}

        # Send the POST request to the FastAPI backend
        headers = {"accept": "application/json"}

        # Use `requests.post` to send the request with JSON and file together
        response = None
        if uploaded_file:
            # Use multipart form-data to handle both file and JSON data
            response = requests.post(f"{BASE_API_URL}/analyze_attachment", headers=headers, files=files)
        else:
            # Just send the JSON data if no file is uploaded
            response = requests.post(f"{BASE_API_URL}/generate_insights", headers=headers, json=request_payload)

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
