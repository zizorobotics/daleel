import re

def clean_and_structure(text_blocks):
    """
    Cleans OCR text and structures it into meaningful fields dynamically.
    """
    structured_data = {}

    for text in text_blocks:
        if "ministry of interior" in text.lower():
            structured_data["header"] = text
        elif re.search(r"\b\d{9,12}\b", text):
            structured_data["license_no"] = text
        elif re.search(r"\b\d{2}/\d{2}/\d{4}\b", text):
            if "issue" in text.lower():
                structured_data["date_issue"] = text
            elif "expiry" in text.lower():
                structured_data["date_expiry"] = text
            else:
                structured_data["date_birth"] = text
        elif re.search(r"\b[A-Z\s]+\b", text) and "nationality" not in text.lower():
            structured_data["name"] = text
        elif re.search(r"\b[A-Z]{3}\b", text):
            structured_data["nationality"] = text

    return structured_data

# Example Usage:
# cleaned_data = clean_and_structure(["Ministry of Interior", "11/01/2021", "IND"])
