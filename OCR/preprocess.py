import cv2
import numpy as np

def preprocess_image(image_path):
    """Preprocess image to improve OCR accuracy."""

    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        raise FileNotFoundError(f"OpenCV could not load image: {image_path}. Check file path and format.")

    # Resize for better OCR performance
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    # Denoising to remove unnecessary noise
    img = cv2.fastNlMeansDenoising(img, h=30)

    # Adaptive Thresholding for better text extraction
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                cv2.THRESH_BINARY, 31, 2)

    # Morphological transformation to make text clearer
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    return img

# Test preprocessing
if __name__ == "__main__":
    import os

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(BASE_DIR, "sample-images", "sample_drivers_license.jpeg")
    processed_img = preprocess_image(image_path)

    # Save processed image for debugging
    output_path = os.path.join(BASE_DIR, "sample-images", "preprocessed_license.jpeg")
    cv2.imwrite(output_path, processed_img)
    print(f"Preprocessed image saved: {output_path}")
