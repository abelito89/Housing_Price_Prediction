"""
Script donde se realizan las graficas del analisis de datos, estas incluyen las siguientes:
- un scatterplot del comportamiento del precio de las casas respecto al area
- un boxplot del precio
- un boxplot del area
- scatterplot del comportamiento del precio segun la cantidad de bedrooms
- variables categoricas en un subplots de 5 filas y 3 columnas

"""
import matplotlib.pyplot as plt

def scatterplot_price_area(df):
    df.plot.scatter(x='area', y='price')    
    return plt.show()


def boxplot_price(df):
    plt.boxplot(df['price'])
    return plt.show()


def boxplot_area (df):
    plt.boxplot(df['area'])
    return plt.show()


def precio_segun_cant_bedrooms(df):
    df.plot.scatter(x='bedrooms', y='price')
    return plt.show()


def precio_segun_cant_bathrooms(df):
    df.plot.scatter(x='bathrooms', y='price')
    return plt.show()


def precio_segun_cant_stories(df):
    df.plot.scatter(x='stories', y='price')
    return plt.show()


def precio_segun_cant_parking (df):
    df.plot.scatter(x='parking', y='price')
    return plt.show()

def histogramas_columnas(df):
    fig, axs = plt.subplots(nrows=5, ncols=3, figsize=(13, 10))
    for ax, column in zip(axs.flat, df.columns):
        ax.hist(df[column])
        ax.set_title(column)
    plt.tight_layout()
    return plt.show()
