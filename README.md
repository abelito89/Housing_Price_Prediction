House Price Prediction
==============================

Practicing with House Price Prediction. Consiste en predecir el precio de una casa con determinadas caracteristicas conocidas. Este es mi primer proyecto en el que abarco todas las fases del proyecto de ciencia de datos:
- limpieza de los datos
- analisis exploratorio de datos
- escalado de los datos con RobustScaler()
- entrenamiento de un Ensemble Learning que combina un SVR con una Regresion Lineal
- despliegue del modelo como una pagina web usando streamlit

## Instalación

Para recrear el entorno virtual donde se desarrolla el proyecto es necesario instalar todo el contenido del archivo requirements.txt
ejecutando en la raiz del proyecto el comando: pip install -r requirements.txt.

## Uso

Para usar el proyecto en localhost se ejecuta en la raiz del proyecto el comando: streamlit run streamlit_app.py
El cual pondra en funcionamiento la web que ve el usuario, donde se le proporcionan las caracteristicas de entrada y el modelo devuelve un valor predicho


<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
