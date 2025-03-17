from pdf2image import convert_from_path
import os

def convert_pdf_to_images(pdf_path, output_folder="temp_images"):
    """
    Converts a PDF file into multiple images (one per page).
    Saves images in the specified output folder.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    images = convert_from_path(pdf_path)
    image_paths = []

    for i, img in enumerate(images):
        image_path = os.path.join(output_folder, f"page_{i+1}.png")
        img.save(image_path, "PNG")
        image_paths.append(image_path)

    return image_paths

# Example Usage:
# image_files = convert_pdf_to_images("sample.pdf")
