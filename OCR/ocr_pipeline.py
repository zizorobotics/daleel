import easyocr
import cv2
from preprocess import detect_text_regions

def extract_text(image_path):
    """
    Dynamically extracts text from detected regions using EasyOCR.
    """
    text_regions = detect_text_regions(image_path)

    reader = easyocr.Reader(['ar', 'en'], gpu=False)
    extracted_texts = []

    for i, region in enumerate(text_regions):
        # Save region for debugging
        temp_path = f"temp_region_{i}.png"
        cv2.imwrite(temp_path, region)

        results = reader.readtext(temp_path, detail=0)
        extracted_texts.append(" ".join(results))

    return extracted_texts

# Example Usage:
# extracted_data = extract_text("image.png")
