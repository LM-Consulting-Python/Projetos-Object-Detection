# Importing required libraries
import pytesseract
from PIL import Image
import cv2

try:
    # Tesseract configuration
    myconfig = r"--psm 1 --oem 3"  # Specific Tesseract configuration

    # Image path
    image_path = r'/Users/felipelm/Documents/GitHub/Projetos-Object-Detection/Extract Text from Images (OCR)/texto.png'

    # Check if the file exists
    if not os.path.isfile(image_path):
        print(f"Error: The file {image_path} does not exist.")
        exit()

    # Perform OCR on the image using Tesseract
    text = pytesseract.image_to_string(Image.open(image_path), config=myconfig)

    # Print the recognized text
    print("Recognized Text:\n", text)

except ModuleNotFoundError as e:
    print(f"Error: The required library is missing. Please install {e.name}.")
