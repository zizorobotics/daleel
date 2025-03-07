import easyocr
import os

def ai_extract_text(image_path):
    """Uses AI-based OCR (EasyOCR) to extract text from an image."""
    reader = easyocr.Reader(['en'])  # Use English OCR
    results = reader.readtext(image_path, detail=0)  
    return " ".join(results)

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(BASE_DIR, "sample-images", "sample_drivers_license.jpeg")

    extracted_text = ai_extract_text(image_path)
    print("AI OCR Extracted Text:\n", extracted_text)
