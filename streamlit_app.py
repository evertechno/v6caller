import requests

base_url = "https://escalyticsv7api.onrender.com"

def analyze_email(email_content, selected_scenario):
    endpoint = f"{base_url}/analyze_email"
    data = {
        "email_content": email_content,
        "selected_scenario": selected_scenario
    }
    response = requests.post(endpoint, json=data)
    return response.json()

def analyze_attachment(file_path):
    endpoint = f"{base_url}/analyze_attachment"
    files = {
        'file': open(file_path, 'rb')
    }
    response = requests.post(endpoint, files=files)
    return response.json()

def analyze_email_attachment(file_path):
    endpoint = f"{base_url}/analyze_email_attachment"
    files = {
        'file': open(file_path, 'rb')
    }
    response = requests.post(endpoint, files=files)
    return response.json()

# Example usage
if __name__ == "__main__":
    email_content = "Your email content here"
    selected_scenario = "Your scenario here"
    
    # Call analyze_email endpoint
    email_analysis_result = analyze_email(email_content, selected_scenario)
    print("Email Analysis Result:")
    print(email_analysis_result)
    
    # Call analyze_attachment endpoint
    attachment_file_path = "path/to/your/attachment.txt"  # Update this path to your actual file
    attachment_analysis_result = analyze_attachment(attachment_file_path)
    print("Attachment Analysis Result:")
    print(attachment_analysis_result)
    
    # Call analyze_email_attachment endpoint
    email_attachment_file_path = "path/to/your/email_attachment.eml"  # Update this path to your actual file
    email_attachment_analysis_result = analyze_email_attachment(email_attachment_file_path)
    print("Email Attachment Analysis Result:")
    print(email_attachment_analysis_result)
