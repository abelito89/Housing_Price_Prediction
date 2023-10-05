import streamlit as st
import pickle 
import pandas as pd
import sys

carga_model = pickle.load(open('../models/model_ensemble_trained.pkl', 'rb'))
carga_robustscaler = pickle.load(open('../models/robust_scaled_trained.pkl', 'rb'))

def scaling(carga_robustscaler,df_num):
    return carga_robustscaler.fit_transform(df_num)


def prediction(carga_model,df_scaled):
    return carga_model.predict(df_scaled)


def main():
    st.title('Housing Price Prediction')
    st.header('Parametros de prediccion de precios')
    def parametros():
        area = st.number_input("Introduzca el area")
        bedrooms = st.number_input("Introduzca la cantidad de cuartos")
        bathrooms = st.number_input("Introduzca la cantidad de baños")
        stories = st.number_input("Introduzca la cantidad de pisos de la casa")
        mainroad = st.selectbox("La casa esta en una avenida principal?", ["yes","no"])
        guestroom = st.selectbox("La casa tiene cuarto de huespedes?", ["yes","no"])
        basement = st.selectbox("La casa tiene sotano?", ["yes","no"])
        hotwaterheating = st.selectbox("La casa tiene calefaccion por agua?", ["yes","no"])
        airconditioning = st.selectbox("La casa tiene aire acondicionado?", ["yes","no"])
        parking = st.number_input("Introduzca la cantidad de estacionamientos de la casa")
        prefarea = st.selectbox("La casa esta ubicada en un area de preferencia?", ["yes","no"])
        furnishingstatus = st.selectbox("Cual es el estado de moviliario de la casa?", ["furnished","semi-furnished","unfurnished"])
        dict_entrada = {
            "area": area, 
            "bedrooms": bedrooms,
            "bathrooms": bathrooms,
            "stories": stories,
            "mainroad": mainroad,
            "guestroom": guestroom,
            "basement": basement,
            "hotwaterheating": hotwaterheating,
            "airconditioning": airconditioning,
            "parking": parking,
            "prefarea": prefarea,
            "furnishingstatus": furnishingstatus
        }
        df = pd.DataFrame(dict_entrada, index=[0])
        return df
    df = parametros()
    pd.set_option('display.max_columns', None)
    print('PARAMETROS:',df)
    sys.path.append("C:\\Abel\\Trabajo\Proyectos Ciencia de Datos\\House Price Prediction\\src\\data")
    import Transform_cat_a_num_get_dummies
    df_num = Transform_cat_a_num_get_dummies.cat_to_num(df)
    print('df_num:',df_num)
    df_train = pd.read_csv("C:\Abel\Trabajo\Proyectos Ciencia de Datos\House Price Prediction\data\processed\X_train_scaled.csv")
    train_columns = df_train.columns
    if 'Unnamed: 0' in df_train.columns:
        df_train = df_train.drop(columns=['Unnamed: 0'])
    # Asegúrate de que tenga todas las columnas necesarias
    for col in train_columns:
        if col not in df_num.columns:
            df_num[col] = 0

    # Selecciona solo las columnas que estaban en el DataFrame de entrenamiento
    df_num = df_num[train_columns]
    #print(df_train)
    print(df_num)
    # Ahora 'df_num' tiene la misma forma que 'df_train' y puedes usarlo para hacer tu predicción
    
   #df_scaled = scaling(carga_robustscaler,df_num)
    #print(df_num)
    pred = prediction(carga_model,df_num)
    print('La prediccion es:', pred)
    st.write(f'La predicción del precio de la vivienda es: {pred}')


if __name__ == '__main__':
    main()