from ai_ocr import ai_extract_text
from postprocess import clean_and_structure

def process_document(file_path):
    """
    Processes an image file (PNG, JPG) and extracts structured text using AI-based OCR (PaddleOCR).
    """
    extracted_text = ai_extract_text(file_path)  # Use PaddleOCR

    if not extracted_text.strip():
        print("No text detected! Check image quality or OCR settings.")
        return {}

    structured_data = clean_and_structure([extracted_text])  # Convert to structured output

    print("\n--- Extracted Data ---")
    for key, value in structured_data.items():
        print(f"{key}: {value}")

    return structured_data

if __name__ == "__main__":
    file_path = "/Users/adam/Desktop/daleel/OCR/sample-images/sample_wedding_agreement.jpeg"  # Change to your actual document image

    print("\n🔍 Processing document:", file_path)
    process_document(file_path)
