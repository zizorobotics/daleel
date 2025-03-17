from paddleocr import PaddleOCR
import cv2

def ai_extract_text(image_path):
    """
    Uses PaddleOCR to extract Arabic + English text from an image.
    """
    # Load image to verify it exists
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"❌ OpenCV failed to load the image: {image_path}. Check the file path!")

    # Initialize PaddleOCR with Arabic & English support
    ocr = PaddleOCR(lang="ar", use_angle_cls=True)

    # Perform OCR on a SINGLE image (NOT a list)
    results = ocr.ocr(image_path, cls=True, det=True, rec=True)

    extracted_text = []
    if results and isinstance(results, list):
        for result in results:
            if isinstance(result, list):
                for line in result:
                    extracted_text.append(line[1][0])  # Extract detected text

    return " ".join(extracted_text) if extracted_text else "❌ No text detected."

if __name__ == "__main__":
    image_path = "sample_wedding_agreement.jpeg"  # Replace with your actual image
    extracted_text = ai_extract_text(image_path)
    print("\n--- Extracted Text ---")
    print(extracted_text)
