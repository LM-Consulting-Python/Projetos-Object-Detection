# Importação das bibliotecas necessárias
import pytesseract  # Biblioteca para integração com Tesseract OCR
import PIL.Image    # Módulo Pillow para manipulação de imagens
import cv2           # OpenCV para processamento de imagens

# Configuração do Tesseract OCR
myconfig = r"--psm 1 --oem 3"  # Configuração específica do Tesseract

# Caminho para a imagem a ser processada
image_path = r'C:\Users\Felipe LM\Documents\GitHub\Projetos-Object-Detection\Extract Text from Images (OCR)\texto.png'

# Realiza o OCR na imagem usando Tesseract
text = pytesseract.image_to_string(PIL.Image.open(image_path), config=myconfig)

# Exibe o texto reconhecido
print("Texto Reconhecido:\n", text)