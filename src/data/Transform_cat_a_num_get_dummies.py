"""
Modulo que contiene 2 funciones:
cate -> devuelve los nombres de las columnas categoricas
cat_to_num -> toma un dataframe df y transforma las columnas categoricas a numericas
"""
import pandas as pd
def cate(df):
    cat = df.select_dtypes(include=['object','category']).columns
    return cat
