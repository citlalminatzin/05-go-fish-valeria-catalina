import numpy as np
import matplotlib.pyplot as plt
import data   
import main   
import models

#Ejercicio 1
#La explicación de este ejercicio la pueden encontrar en README.md

longitud, peso = read_data("data/pescados.csv")
graficar_longitud_peso(longitud, peso)

# Ejercicio 2

K = main.similitud_geometrica(longitud.tolist(), peso.tolist())
print(f"Valor de K estimado: {K:.8f}")
x = longitud ** 3
rho = models.pearson(x.tolist(), peso.tolist())
print(f"Coeficiente de Pearson: {rho:.4f}")
#Gráfica
models.graficar_ej2(x=x.tolist(), y=peso.tolist(), k=K, titulo='Modelo de Similitud Geométrica: Peso vs Longitud al Cubo')