# Importing required libraries
import pytesseract
from PIL import Image
import cv2

# Configuring Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_tesseract_executable>'
config = ("-l eng --psm 6")  # Using English language and setting page segmentation mode

# Path to the image to be processed
image_path = r'<full_path_to_image_file>'

# Reading the image with OpenCV
image = cv2.imread(image_path)
height, width, _ = image.shape

# Pre-processing the image for better OCR results
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.GaussianBlur(image, (5, 5), 0)

# Using pytesseract to extract text from the image
text = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT, config=config)

# Iterating through the found text boxes
for i in range(len(text['text'])):
    # Filtering text boxes with confidence greater than 60
    if int(text['conf'][i]) > 60:
        # Getting coordinates and dimensions of the text box
        (x, y, width, height) = (text['left'][i], text['top'][i], text['width'][i], text['height'][i])

        # Drawing a rectangle around the text box
        image = cv2.rectangle(image, (x, y), (x+width, y+height), (0, 255, 0), 2)

        # Adding recognized text to the image
        image = cv2.putText(image, text['text'][i], (x, y+height+20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2, cv2.LINE_AA)

# Displaying the image with text boxes and recognized text
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
