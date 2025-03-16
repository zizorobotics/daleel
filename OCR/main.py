from ocr_pipeline import extract_text
from postprocess import clean_and_structure

def process_document(file_path):
    """
    Processes an image file (PNG, JPG) and extracts structured text.
    """
    extracted_texts = extract_text(file_path)  # Extract text from PNG
    structured_data = clean_and_structure(extracted_texts)  # Structure output

    return structured_data

if __name__ == "__main__":
    file_path = "/Users/adam/Desktop/daleel/OCR/sample-images/sample_drivers_license.jpeg"  # Change this to your actual image file
    structured_output = process_document(file_path)

    print("\n--- Extracted Data ---")
    for key, value in structured_output.items():
        print(f"{key}: {value}")
