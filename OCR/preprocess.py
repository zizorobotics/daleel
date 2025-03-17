import cv2
import numpy as np

def detect_text_regions(image_path):
    """
    Enhanced Arabic and English text preprocessing for OCR.
    """
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Increase contrast to enhance Arabic text
    image = cv2.equalizeHist(image)

    # Resize for better readability
    image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    # Apply Bilateral Filter to reduce noise without blurring text
    image = cv2.bilateralFilter(image, 9, 75, 75)

    # Adaptive Thresholding (Preserves Arabic strokes better)
    image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                  cv2.THRESH_BINARY_INV, 15, 3)

    # Morphological Closing to strengthen Arabic strokes
    kernel = np.ones((2, 2), np.uint8)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

    # Find contours (text regions)
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    text_regions = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)

        # Filter out small artifacts
        if w > 40 and h > 10:
            cropped = image[y:y+h, x:x+w]
            text_regions.append(cropped)

    return text_regions
