import pandas as pd
import pickle


def predict_model(df):
    # Cargar el modelo entrenado desde un archivo .pkl
    with open('models/model_ensemble_trained.pkl', 'rb') as file:
        model = pickle.load(file)
    # Hacer predicciones con el modelo
    predictions = model.predict(df)
    # Guardar las predicciones en un archivo .csv
    return pd.DataFrame(predictions).to_csv('predictions.csv', index=False)