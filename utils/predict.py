from joblib import load
import numpy as np

model, class_names = load("model/classifier.pkl")

def extract_features(image):
    return image.flatten().reshape(1, -1)

def predict_image(image):
    features = extract_features(image)
    prediction = model.predict(features)
    return class_names[prediction[0]]
