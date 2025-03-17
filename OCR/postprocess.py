import re
import bidi.algorithm as bidi
from arabic_reshaper import reshape

def clean_and_structure(text_blocks):
    """
    Cleans OCR text and structures it, ensuring Arabic text is reshaped and displayed correctly.
    """
    structured_data = {}

    for text in text_blocks:
        # Fix Arabic text issues
        if re.search(r"[\u0600-\u06FF]", text):  # Detect Arabic text
            reshaped_text = reshape(text)  # Fix character order
            formatted_text = bidi.get_display(reshaped_text)  # Fix right-to-left display
            structured_data["arabic_text"] = formatted_text
        elif "ministry of interior" in text.lower():
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
