import os
import cv2 # manipulação de imagens
import numpy as np
from sklearn.ensemble import RandomForestClassifier # modelo de classificação
from sklearn.model_selection import train_test_split # divisão dos dados em treino e teste
from sklearn.metrics import classification_report # relatório de classificação
from joblib import dump # salvar o modelo treinado

# Caminho para as imagens
DATASET_DIR = "data/dataset"
IMG_SIZE = (150, 150)


X, y = [], [] # listas para armazenar as imagens e os rótulos
class_names = os.listdir(DATASET_DIR)
print(f"Classes encontradas: {class_names}")

for idx, class_name in enumerate(class_names):
    class_folder = os.path.join(DATASET_DIR, class_name)
    for filename in os.listdir(class_folder):
        file_path = os.path.join(class_folder, filename)
        try:
            img = cv2.imread(file_path)
            img = cv2.resize(img, IMG_SIZE)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            X.append(img.flatten())  # transforma em vetor
            y.append(idx)
        except:
            print(f"Erro ao processar: {file_path}")

# Converter listas para arrays numpy (isso é necessário para o scikit-learn)
X = np.array(X)
y = np.array(y)

# Dividir em treino/teste com estratificação
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Treinar o modelo
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Avaliação
y_pred = model.predict(X_test)
print("\nRELATÓRIO:")
print(classification_report(y_test, y_pred, target_names=class_names))

# Salvar modelo + nomes das classes
dump((model, class_names), "model/classifier.pkl")
print("\nModelo salvo em model/classifier.pkl")
