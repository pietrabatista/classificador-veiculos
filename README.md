# Classificador de Veículos com Interface Gráfica (GUI)

Este projeto é uma aplicação em Python que permite ao usuário **classificar imagens de veículos** usando:

- Imagens capturadas pela **webcam**
- Imagens carregadas do **computador local**

O classificador foi treinado para distinguir entre três tipos de veículos:

- **Carro**
- **Bicicleta**
- **Ônibus**

---

## Demonstração em Vídeo

Assista ao funcionamento completo do projeto neste vídeo:

[Clique aqui para assistir no Google Drive](https://drive.google.com/file/d/1nQdQZaKo8SzP5cTlELAEeUp8yEjY1xMZ/view?usp=sharing)

Obs: Sugiro assistir em 2.0x ou ir direto para o minuto 3 caso queira ver somente a implementação com a interface.

---

## Algoritmo e Funcionamento

- **Modelo:** `RandomForestClassifier` do `scikit-learn`
- **Entrada:** imagens coloridas redimensionadas para **150x150 pixels**
- **Saída:** nome da classe prevista com base na imagem

---

## Desempenho

O modelo foi treinado com 60 imagens no total, sendo:

- 20 imagens de carros
- 20 imagens de bicicletas
- 20 imagens de ônibus

Após o treino com separação de 80% para treino e 20% para teste, obtivemos os seguintes resultados:

#### Exemplo de resultados:

```

RELATÓRIO:
              precision    recall  f1-score   support

   bicicleta       1.00      0.50      0.67
       carro       1.00      0.50      0.67
      onibus       0.50      1.00      0.67

    accuracy                           0.67

```

Acurácia: **67%**

- Isso significa que o modelo acertou 2 em cada 3 imagens durante o teste.

- Embora não seja um valor extremamente alto, é adequado para um dataset pequeno e com imagens variadas.

- A performance pode ser melhorada com:

    - Mais imagens para cada classe

    - Pré-processamento (ex: normalização, filtros)

    - Extração de features mais robusta (ex: HOG, CNN)

---

## Tecnologias Utilizadas

- Python 3
- [scikit-learn](https://scikit-learn.org/)
- [PySimpleGUI](https://pysimplegui.readthedocs.io/)
- OpenCV (`cv2`)
- Pillow (`PIL`)
- joblib

---

## Como Usar

### 1. Clone o repositório e entre na pasta

```bash
git clone https://github.com/pietrabatista/classificador-veiculos.git
cd classificador-veiculos
```
### 2. Crie o ambiente virtual e ative

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instale os pacotes necessários

```bash
pip install -r requirements.txt
```

### 4. Treine o modelo

Certifique-se de que as imagens estão organizadas assim:

```bash
data/dataset
├── bicicleta/
│   ├── 1.jpg
│   └── ...
├── carro/
│   └── ...
└── onibus/
    └── ...
```
E execute:

```bash
python train.py
```

### 5. Execute o visualizador

```bash
python gui/app.py
```

### Estrutura do Projeto

```
ponderada_classificador/
├── data/
│   └── dataset/
├── gui/
│   └── app.py
├── model/
│   └── classifier.pkl
├── utils/
│   └── predict.py
├── train.py
├── requirements.txt
└── README.md
```






