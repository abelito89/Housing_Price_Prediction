import streamlit as st
import pickle 
import pandas as pd
import sys

carga_model = pickle.load(open('../models/model_ensemble_trained.pkl', 'rb'))
carga_robustscaler = pickle.load(open('../models/robust_scaled_trained.pkl', 'rb'))

def scaling(carga_robustscaler,df):
    return carga_robustscaler.fit_transform(df)


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
        if mainroad == "yes":
            mainroad_yes = "1"
            mainroad_no = "0"
        else:
            mainroad_yes = "0"
            mainroad_no = "1"            
        
        guestroom = st.selectbox("La casa tiene cuarto de huespedes?", ["yes","no"])
        if guestroom == "yes":
            guestroom_yes = "1"
            guestroom_no = "0"
        else:
            guestroom_yes = "0"
            guestroom_no = "1" 
        basement = st.selectbox("La casa tiene sotano?", ["yes","no"])
        if basement == "yes":
            basement_yes = "1"
            basement_no = "0"
        else:
            basement_yes = "0"
            basement_no = "1" 
        hotwaterheating = st.selectbox("La casa tiene calefaccion por agua?", ["yes","no"])
        if hotwaterheating == "yes":
            hotwaterheating_yes = "1"
            hotwaterheating_no = "0"
        else:
            hotwaterheating_yes = "0"
            hotwaterheating_no = "1"
        airconditioning = st.selectbox("La casa tiene aire acondicionado?", ["yes","no"])
        if airconditioning == "yes":
            airconditioning_yes = "1"
            airconditioning_no = "0"
        else:
            airconditioning_yes = "0"
            airconditioning_no = "1"
        parking = st.number_input("Introduzca la cantidad de estacionamientos de la casa")
        prefarea = st.selectbox("La casa esta ubicada en un area de preferencia?", ["yes","no"])
        if prefarea == "yes":
            prefarea_yes = "1"
            prefarea_no = "0"
        else:
            prefarea_yes = "0"
            prefarea_no = "1"
        furnishingstatus = st.selectbox("Cual es el estado de moviliario de la casa?", ["furnished","semi-furnished","unfurnished"])
        if furnishingstatus == "furnished":
            furnishingstatus_furnished = "1"
            furnishingstatus_semi_furnished = "0"
            furnishingstatus_unfurnished = "0"

        elif furnishingstatus == "semi-furnished":
            furnishingstatus_furnished = "0"
            furnishingstatus_semi_furnished = "1"
            furnishingstatus_unfurnished = "0"
        else:
            furnishingstatus_furnished = "0"
            furnishingstatus_semi_furnished = "0"
            furnishingstatus_unfurnished = "1"
        dict_entrada = {
            "area": area, 
            "bedrooms": bedrooms,
            "bathrooms": bathrooms,
            "stories": stories,
            "parking": parking,            
            "mainroad_no": mainroad_no,
            "mainroad_yes": mainroad_yes,            
            "guestroom_no": guestroom_no,
            "guestroom_yes": guestroom_yes,            
            "basement_no": basement_no,
            "basement_yes": basement_yes,            
            "hotwaterheating_no": hotwaterheating_no,
            "hotwaterheating_yes": hotwaterheating_yes,            
            "airconditioning_no": airconditioning_no,
            "airconditioning_yes": airconditioning_yes,        
            "prefarea_no": prefarea_no,
            "prefarea_yes": prefarea_yes,
            "furnishingstatus_furnished": furnishingstatus_furnished,
            "furnishingstatus_semi-furnished": furnishingstatus_semi_furnished,
            "furnishingstatus_unfurnished": furnishingstatus_unfurnished
        }
        df = pd.DataFrame(dict_entrada, index=[0])
        return df
    df = parametros()
    pd.set_option('display.max_columns', None)
    
    sys.path.append("C:\\Abel\\Trabajo\Proyectos Ciencia de Datos\\House Price Prediction\\src\\data")
    
    df_scaled = scaling(carga_robustscaler,df)
    pred = prediction(carga_model,df_scaled)
    print('La prediccion es:', pred)
    st.write(f'La predicción del precio de la vivienda es: {pred}')


if __name__ == '__main__':
    main()