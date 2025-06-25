import sys
import io
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import PySimpleGUI as sg # interface gráfica
import cv2 # manipulação de imagens
import numpy as np # manipulação de arrays
from PIL import Image # converter imagem para bytes
from utils.predict import predict_image # função de predição

# redimensionar imagem para o tamanho esperado pelo modelo
def resize_image(image, size=(150, 150)):
    return cv2.resize(image, size)

# converter imagem de array numpy para bytes (no formato PNG suportado pelo PySimpleGUI)
def convert_to_bytes(img_array):
    img = Image.fromarray(img_array)
    with io.BytesIO() as output:
        img.save(output, format="PNG")
        return output.getvalue()

# Configuração do tema e layout da janela
sg.theme("DarkBlue3")  # tema da janela
layout = [
    [sg.Text("Classificador de Imagens")],
    [sg.Image(key="-IMAGE-")],
    [sg.Button("Upload de Imagem"), sg.Button("Utilizar Webcam"), sg.Button("Sair")],
    [sg.Text("Categoria:", size=(10, 1)), sg.Text("", key="-OUTPUT-")]
]

window = sg.Window("Visualizador", layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "Sair"):
        break

    # abre o explorador de arquivos para upload de imagem 
    elif event == "Upload de Imagem":
        file_path = sg.popup_get_file("Escolha uma imagem", file_types=(("Imagens", "*.png;*.jpg;*.jpeg"),))
        if file_path:
            img = cv2.imread(file_path) # lê a imagem
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img_resized = resize_image(img_rgb) 
            img_bytes = convert_to_bytes(img_resized)
            prediction = predict_image(img_resized) # predição da imagem
            window["-IMAGE-"].update(data=img_bytes) # atualiza a imagem na janela
            window["-OUTPUT-"].update(prediction) # atualiza o texto com a categoria prevista

    elif event == "Utilizar Webcam":
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            sg.popup_error("Não foi possível abrir a câmera.")
            continue

        sg.popup("Pressione ESPAÇO na janela da webcam para capturar.")
        while True:
            ret, frame = cap.read()
            if not ret:
                sg.popup_error("Erro ao ler da câmera.")
                break

            cv2.imshow("Pressione ESPAÇO para capturar / ESC para sair", frame)
            key = cv2.waitKey(1)

            if key == 27:  # ESC
                frame = None
                break
            elif key == 32:  # ESPAÇO
                break

        cap.release()
        cv2.destroyAllWindows()

        if frame is not None:
            img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img_resized = resize_image(img_rgb)
            img_bytes = convert_to_bytes(img_resized)
            prediction = predict_image(img_resized)
            window["-IMAGE-"].update(data=img_bytes)
            window["-OUTPUT-"].update(prediction)
        else:
            sg.popup("Captura cancelada.")

window.close()
