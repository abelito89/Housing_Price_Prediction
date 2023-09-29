"""
Este es el script principal donde se ejecutara todo el proyecto ejecutando funciones definidas en los diferentes modulos
"""
import sys
sys.path.append("C:\\Abel\\Trabajo\\Proyectos Ciencia de Datos\\House Price Prediction\\src\\visualization")
sys.path.append("C:\\Abel\\Trabajo\\Proyectos Ciencia de Datos\\House Price Prediction\\src\\data")
sys.path.append("C:\\Abel\\Trabajo\\Proyectos Ciencia de Datos\\House Price Prediction\\src\\models")
import visualize
import carga_datos
import Transform_cat_a_num_get_dummies
import train_model


def visualizations(df):
    visualize.scatterplot_price_area(df)
    visualize.boxplot_price(df)
    visualize.boxplot_area(df)
    visualize.precio_segun_cant_bedrooms(df)
    visualize.precio_segun_cant_bathrooms(df)
    visualize.precio_segun_cant_stories(df)
    visualize.precio_segun_cant_parking(df)
    visualize.histogramas_columnas(df)


def main():
    df = carga_datos.carga_datos('C:\\Abel\\Trabajo\\Proyectos Ciencia de Datos\\House Price Prediction\\data\\processed\\Housing.csv')
    print("Las variable categoricas son: ",Transform_cat_a_num_get_dummies.cate(df))
    df_num = Transform_cat_a_num_get_dummies.cat_to_num(df)
    X,y = train_model.sep_X_de_y(df_num)
    train_set, val_set, test_set = train_model.train_val_test_split(df_num)
    X_train, y_train, X_test, y_test, X_val, y_val = train_model.sep_X_de_y_train_val_test(train_set, val_set, test_set)
    X_train_scaled, X_val_scaled, X_test_scaled = train_model.scal_robust_scaler(X_train, X_test, X_val)
    modelo_entrenado = train_model.ensemble_reg_lineal_svr(X_train_scaled, y_train)
    validation = train_model.val_R2_score(modelo_entrenado,X_val_scaled, y_val)
    print("EL R2_score del modelo con el set de validacion es:", validation)
    prueba = train_model.val_R2_score(modelo_entrenado,X_test_scaled, y_test)
    print("EL R2_score del modelo con el set de prueba es:", prueba)

if __name__ == "__main__":
    main()