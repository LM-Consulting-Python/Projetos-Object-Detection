# Importação das bibliotecas necessárias
import pytesseract  # Biblioteca para integração com Tesseract OCR
from pytesseract import Output
import PIL.Image    # Módulo Pillow para manipulação de imagens
import cv2           # OpenCV para processamento de imagens

# Configuração do Tesseract OCR
myconfig = r"--psm 1 --oem 3"  # Configuração específica do Tesseract

# Caminho para a imagem a ser processada
image_path = r'C:\Users\Felipe LM\Documents\GitHub\Projetos-Object-Detection\Extract Text from Images (OCR)\texto.png'

# Lê a imagem com OpenCV
img = cv2.imread(image_path)
height, width, _ = img.shape

# Utiliza pytesseract para obter dados de texto na imagem
data = pytesseract.image_to_data(img, config=myconfig, output_type=Output.DICT)

# Obtém a quantidade de caixas de texto encontradas
amount_boxes = len(data['text'])

# Itera sobre as caixas de texto
for i in range(amount_boxes):
    # Filtra caixas de texto com confiança maior que 20
    if float(data['conf'][i]) > 20:
        # Obtém coordenadas e dimensões da caixa
        (x, y, width, height) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])

        # Desenha um retângulo ao redor da caixa de texto
        img = cv2.rectangle(img, (x, y), (x+width, y+height), (0, 255, 0), 2)

        # Adiciona texto reconhecido à imagem
        img = cv2.putText(img, data['text'][i], (x, y+height+20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2, cv2.LINE_AA)

# Exibe a imagem com as caixas de texto e texto reconhecido
cv2.imshow("img", img)
cv2.waitKey(0)