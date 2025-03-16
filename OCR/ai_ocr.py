import easyocr
from preprocess import preprocess_image  # Import preprocessing function

def ai_extract_text(image_path):
    """
    Uses AI-based OCR (EasyOCR) to extract text from an image.
    Applies preprocessing before extraction for better accuracy.
    """
    # Preprocess the image before OCR
    processed_image_path = preprocess_image(image_path)

    # Initialize EasyOCR reader **only for English**
    reader = easyocr.Reader(['en'], gpu=False)  # Removed 'ar'

    # Perform OCR on the preprocessed image
    results = reader.readtext(processed_image_path, detail=0)

    return " ".join(results)

# Example Usage:
if __name__ == "__main__":
    image_path = "/Users/adam/Desktop/daleel/OCR/sample-images/sample_drivers_license.jpeg"
    extracted_text = ai_extract_text(image_path)
    print("Extracted Text:\n", extracted_text)
