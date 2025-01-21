# Data wrangling
import math
import numpy as np
import pandas as pd
# Visualización de datos
import seaborn as sns
import matplotlib.pyplot as plt


def plot_histograms(df, variables, filename, n_cols=5):
    '''Función para graficar histogramas y crear una imagen png con esas gráficas'''
    sns.set(style="whitegrid")
    # Calcula el número de filas necesarias para una grilla de 5 columnas
    n_rows = math.ceil(len(variables) / n_cols)
    # Crear una grilla para los histogramas
    fig, axs = plt.subplots(nrows=n_rows, ncols=n_cols, figsize=(20, 4 * n_rows))
    # Aplanar el arreglo de ejes para una iteración más fácil
    axs = axs.flatten()
    for i, var in enumerate(variables):
        sns.histplot(data=df, x=var, kde=True, ax=axs[i])
        axs[i].set_title(f'Histograma de {var}')
    # Ocultar los ejes que no se usan, si los hay
    for ax in axs[i + 1:]:
        ax.set_visible(False)
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.show()

def freq_discrete(df, features):
    '''Función para graficar las tablas de frecuencias de las variables categóricas'''
    for feature in features:
        print(f"Variable: {feature}")
        abs_ = df[feature].value_counts(dropna=False).to_frame().rename(columns={"count": "Frecuencia absoluta"})
        rel_ = df[feature].value_counts(dropna=False, normalize= True).to_frame().rename(columns={"proportion": "Frecuencia relativa"})
        freq = abs_.join(rel_)
        freq["Frecuencia acumulada"] = freq["Frecuencia absoluta"].cumsum()
        freq["Frecuencia relativa acumulada"] = freq["Frecuencia relativa"].cumsum()
        freq["Frecuencia absoluta"] = freq["Frecuencia absoluta"].map(lambda x: "{:,.0f}".format(x))
        freq["Frecuencia relativa"] = freq["Frecuencia relativa"].map(lambda x: "{:,.2%}".format(x))
        freq["Frecuencia acumulada"] = freq["Frecuencia acumulada"].map(lambda x: "{:,.0f}".format(x))
        freq["Frecuencia relativa acumulada"] = freq["Frecuencia relativa acumulada"].map(lambda x: "{:,.2%}".format(x))
        display(freq)

def plot_pie(df, categorical_variables, n_cols, filename):
    '''Funcion para graficar diagramas de pastel'''
    #n_cols = 5 # Número de columnas en la grilla
    n_rows = math.ceil(len(categorical_variables) / n_cols) # Número de filas necesarias para acomodar tod
    # Crear la grilla de gráficos
    fig, axs = plt.subplots(nrows=n_rows, ncols=n_cols, figsize=(n_cols * 4, n_rows * 4)) # Ajusta el tama
    # Aplanar el arreglo de ejes para una iteración más fácil
    axs = axs.flatten()
    # Crear cada gráfico de pastel
    for i, var in enumerate(categorical_variables):
        # Contar las ocurrencias de cada categoría
        counts = df[var].value_counts()
        # Crear el gráfico de pastel
        axs[i].pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=140)
        axs[i].set_title(f'{var}')
    # Ocultar los ejes que no se usan
    for ax in axs[i+1:]:
        ax.set_visible(False)
    plt.tight_layout()
    # Opcional: Guardar la figura en un archivo PNG
    plt.savefig(filename, dpi=300) # Ajusta la resolución (dpi) según sea necesario
    plt.show()