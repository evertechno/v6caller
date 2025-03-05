import streamlit as st
import requests
import json

# Base URL of the API hosted on Render
API_URL = "https://v6api.onrender.com"

# Function to call the /analyze endpoint
def analyze_email(email_content, features, scenario):
    url = f"{API_URL}/analyze"
    headers = {"Content-Type": "application/json"}
    
    # Create payload for the API request
    payload = {
        "email_content": email_content,
        "features": features,
        "scenario": scenario
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error: {response.status_code} - {response.text}")
        return None

# Streamlit app layout and components
st.title("📧 Email Analysis & Insights")
st.write("Welcome to the Email Analysis and Insights web app!")

# Email content input
email_content = st.text_area("📩 Paste your email content here:", height=200)

# Define available features
features = {
    "sentiment": st.checkbox("Sentiment Analysis", value=True),
    "highlights": st.checkbox("Key Highlights", value=True),
    "response": st.checkbox("Suggested Response", value=True),
    "tone": st.checkbox("Email Tone", value=True),
    "tasks": st.checkbox("Actionable Tasks", value=True),
    "subject": st.checkbox("Suggested Subject Line", value=True),
    "clarity": st.checkbox("Clarity Rating", value=True),
    "complexity_reduction": st.checkbox("Simplified Explanation", value=True),
    "scenario_responses": st.checkbox("Scenario-Based Response", value=True),
    "attachment_analysis": st.checkbox("Attachment Analysis", value=True),
    "phishing_detection": st.checkbox("Phishing Detection", value=True),
    "sensitive_info_detection": st.checkbox("Sensitive Information Detection", value=True),
    "confidentiality_rating": st.checkbox("Confidentiality Rating", value=True),
    "bias_detection": st.checkbox("Bias Detection", value=True),
    "conflict_detection": st.checkbox("Conflict Detection", value=True),
    "argument_mining": st.checkbox("Argument Mining", value=True),
}

# Select a scenario for the response
scenario_options = [
    "Customer Complaint", "Product Inquiry", "Billing Issue", "Technical Support Request", 
    "General Feedback", "Order Status", "Shipping Delay", "Refund Request", 
    "Product Return", "Product Exchange", "Payment Issue", "Subscription Inquiry", 
    "Account Recovery", "Account Update Request", "Cancellation Request", "Warranty Claim",
    "Product Defect Report", "Delivery Problem", "Product Availability", "Store Locator", 
    "Service Appointment Request", "Installation Assistance", "Upgrade Request", 
    "Compatibility Issue", "Product Feature Request", "Product Suggestions", 
    "Customer Loyalty Inquiry", "Discount Inquiry", "Coupon Issue", "Service Level Agreement (SLA) Issue", 
    "Invoice Clarification", "Tax Inquiry", "Refund Policy Inquiry", "Order Modification Request", 
    "Credit Card Authorization Issue", "Security Inquiry", "Privacy Concern", 
    "Product Manual Request", "Shipping Address Change", "Customer Support Availability Inquiry", 
    "Live Chat Issue", "Email Support Response Inquiry", "Online Payment Gateway Issue", 
    "E-commerce Website Bug Report", "Technical Documentation Request", "Mobile App Issue", 
    "Software Update Request", "Product Recall Notification", "Urgent Request"
]
scenario = st.selectbox("Select a scenario for suggested response:", scenario_options)

# Button to trigger API request
if st.button("🔍 Analyze Email"):
    if email_content:
        with st.spinner("Analyzing... Please wait..."):
            # Call the API to analyze the email content with selected features and scenario
            analysis_result = analyze_email(email_content, features, scenario)

            if analysis_result:
                st.subheader("📌 Analysis Results")

                # Show analysis results based on features selected
                if "summary" in analysis_result:
                    st.subheader("📋 Email Summary")
                    st.write(analysis_result["summary"])

                if "response" in analysis_result:
                    st.subheader("✉️ Suggested Response")
                    st.write(analysis_result["response"])

                if "highlights" in analysis_result:
                    st.subheader("🔑 Key Highlights")
                    st.write(analysis_result["highlights"])

                if "sentiment" in analysis_result:
                    st.subheader("💬 Sentiment Analysis")
                    st.write(f"**Sentiment:** {analysis_result['sentiment']}")

                if "tone" in analysis_result:
                    st.subheader("🎭 Email Tone")
                    st.write(analysis_result["tone"])

                if "tasks" in analysis_result:
                    st.subheader("📝 Actionable Tasks")
                    st.write(analysis_result["tasks"])

                if "subject" in analysis_result:
                    st.subheader("📬 Subject Line Recommendation")
                    st.write(analysis_result["subject"])

                if "clarity" in analysis_result:
                    st.subheader("🔍 Clarity Rating")
                    st.write(f"Clarity: {analysis_result['clarity']}")

                if "complexity_reduction" in analysis_result:
                    st.subheader("🔽 Simplified Explanation")
                    st.write(analysis_result["complexity_reduction"])

                if "scenario_response" in analysis_result:
                    st.subheader("📜 Scenario-Based Suggested Response")
                    st.write(f"**{scenario}:**")
                    st.write(analysis_result["scenario_response"])

                if "attachment_analysis" in analysis_result:
                    st.subheader("📎 Attachment Analysis")
                    st.write(analysis_result["attachment_analysis"])

                if "phishing_detection" in analysis_result:
                    st.subheader("⚠️ Phishing Links Detected")
                    st.write(analysis_result["phishing_detection"])

                if "sensitive_info_detection" in analysis_result:
                    st.subheader("⚠️ Sensitive Information Detected")
                    st.json(analysis_result["sensitive_info_detection"])

                if "confidentiality_rating" in analysis_result:
                    st.subheader("🔐 Confidentiality Rating")
                    st.write(f"Confidentiality Rating: {analysis_result['confidentiality_rating']}/5")

                if "bias_detection" in analysis_result:
                    st.subheader("⚖️ Bias Detection")
                    st.write(analysis_result["bias_detection"])

                if "conflict_detection" in analysis_result:
                    st.subheader("🚨 Conflict Detection")
                    st.write(analysis_result["conflict_detection"])

                if "argument_mining" in analysis_result:
                    st.subheader("💬 Argument Mining")
                    st.write(analysis_result["argument_mining"])
    else:
        st.error("⚠️ Please provide the email content before analyzing.")
