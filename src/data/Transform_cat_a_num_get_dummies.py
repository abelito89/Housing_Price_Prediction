"""
Modulo que contiene 2 funciones:
cate -> devuelve los nombres de las columnas categoricas
cat_to_num -> toma un dataframe df y transforma las columnas categoricas a numericas
"""
import pandas as pd
def cate(df):
    cat = df.select_dtypes(include=['object','category']).columns
    return cat

def cat_to_num(df):
    df_num = pd.DataFrame(pd.get_dummies(df, columns=['mainroad','guestroom','basement','hotwaterheating','airconditioning','prefarea','furnishingstatus']))
    bool_cols = df_num.select_dtypes(include='bool').columns
    df_num[bool_cols] = df_num[bool_cols].astype(int)
    return df_num