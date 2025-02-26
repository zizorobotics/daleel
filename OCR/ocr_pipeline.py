import pytesseract
from preprocess import preprocess_image
import cv2

def extract_text(image_path):
    """Extracts text from a preprocessed image using optimized Tesseract OCR."""
    processed_img = preprocess_image(image_path)

    # Set Tesseract configuration
    custom_config = r'--oem 3 --psm 6'  # Use OCR Engine Mode 3, Page Segmentation Mode 6

    text = pytesseract.image_to_string(processed_img, config=custom_config)
    return text.strip()

if __name__ == "__main__":
    import os

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(BASE_DIR, "sample-images", "preprocessed_license.jpeg")

    extracted_text = extract_text(image_path)
    print("📝 Extracted Text:\n", extracted_text)
