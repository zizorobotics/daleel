import cv2
import numpy as np

def detect_text_regions(image_path):
    """
    Detects text regions dynamically using OpenCV contours.
    Returns cropped text regions as images.
    """
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Resize for better OCR readability
    image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    # Apply Adaptive Thresholding for better text segmentation
    _, thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Find contours (potential text blocks)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    text_regions = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)

        # Filter out small noise
        if w > 50 and h > 10:
            cropped = image[y:y+h, x:x+w]
            text_regions.append(cropped)

    return text_regions

# Example Usage:
# text_blocks = detect_text_regions("image.png")
