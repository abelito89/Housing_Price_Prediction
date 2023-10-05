"""Este es el modulo donde se realiza todo lo relacionado con el entrenamientos del modelo de Machine Learning para
predecir los posibles valores de las casas segun sus caracteristicas de entrada
El modulo consta de 6 funciones:
- sep_X_de_y: toma el dataframe de datos completo y lo divide en caracteristicas(X) y variable de salida o etiqueta(y)
- train_val_test_split: divide el dataframe de datos en los sets de entrenamiento(train), validacion(val) y prueba(test)
- sep_X_de_y_train_val_test: divide cada set mencionado en caracteristicas(X) y variable de salida o etiqueta(y) (X_train, y_train, X_test, y_test, X_val, y_val)
- scal_robust_scaler: aplica escalamiento o normalizacion con la clase RobustScaler a los sets de datos con las caracteristicas de entrada (X_train, X_test, X_val)
- ensemble_reg_lineal_svr: entrena el ensemble learning entre una regresion lineal y un svr haciendo seleccion aleatoria de los mejores parametros
- val_R2_score: evalua el coeficiente R2_score del modelo, sirve tanto para set de validacion como para set de prueba
"""


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import VotingRegressor
from scipy.stats import uniform #logra una distribucion igualmente probable del parametro que se le especifique
from sklearn.model_selection import RandomizedSearchCV
import pickle


def sep_X_de_y(df_num):
    X = df_num.drop('price',axis=1)
    y = df_num['price'].copy()
    return X,y


def train_val_test_split(df_num):
    train_set, df_test_val = train_test_split(df_num, test_size=0.4, train_size=None, random_state=42, shuffle=True, stratify=None)
    test_set, val_set = train_test_split (df_test_val, test_size = 0.5, random_state = 42, shuffle = False, stratify = None)
    return train_set, val_set, test_set


def sep_X_de_y_train_val_test(train_set, val_set, test_set):
    X_train = train_set.drop('price', axis=1)
    y_train = train_set['price'].copy()
    X_test = test_set.drop('price', axis=1)
    y_test = test_set['price'].copy()
    X_val = val_set.drop('price', axis=1)
    y_val = val_set['price'].copy()
    return X_train, y_train, X_test, y_test, X_val, y_val


def scal_robust_scaler(X_train, X_test, X_val):
    from sklearn.preprocessing import RobustScaler
    robustscaler = RobustScaler()
    X_train_scaled = robustscaler.fit_transform(X_train)
    X_train_scaled = pd.DataFrame(X_train_scaled, columns=X_train.columns)
    X_val_scaled = robustscaler.transform(X_val)
    X_val_scaled = pd.DataFrame(X_val_scaled)
    X_test_scaled = robustscaler.transform(X_test)
    X_test_scaled = pd.DataFrame(X_test_scaled)
    with open('models/robust_scaled_trained.pkl', 'wb') as file:
        pickle.dump(robustscaler, file)
    X_train_scaled.to_csv('X_train_scaled.csv',index=False,header=True)
    return X_train_scaled, X_val_scaled, X_test_scaled


def ensemble_reg_lineal_svr(X_train_scaled, y_train):
    svr = SVR()
    lin_reg = LinearRegression()
    ensemble_reg = VotingRegressor(estimators=[('linear', lin_reg), ('svr', svr)], weights=[0.4, 0.6])
    param_distributions = {'linear__fit_intercept': [True, False], 'svr__C': uniform(1, 100000), 'svr__kernel': ['linear', 'poly', 'rbf', 'sigmoid']}
    rand_search = RandomizedSearchCV(ensemble_reg, param_distributions, n_iter=50, scoring='r2', cv=5)
    return rand_search.fit(X_train_scaled, y_train)

def val_R2_score(modelo_entrenado,X_val_scaled, y_val):
    best_model = modelo_entrenado.best_estimator_
    r2_score = best_model.score(X_val_scaled, y_val)
    return r2_score


def RobustScaled_pickle(RobustScaled):
    with open('models/robust_scaled_trained.pkl', 'wb') as file:
        pickle.dump(RobustScaled, file)
    return file


def model_pickle(model):
    with open('models/model_ensemble_trained.pkl', 'wb') as file:
        pickle.dump(model, file)
    return file