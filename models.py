#!/usr/bin/env python
"""
models.py

Es recomendable que escribas unas cuantas líneas
explicando el propósito de cada código. Te propongo
que utilices este archivo para que escribas las
funciones principales que vayas a reutilizar en
tus otras prácticas
"""
import numpy as np
import matplotlib.pyplot as plt
def modelo_geom(longitud: list[float], k: float) -> list[float]:
    """
    Calcula el peso estimado de los róbalos W = K * l^3 
    
    longitudes: list[float] Lista con las medidas de longitud de los peces en cm.
    k: float Constante de proporcionalidad calculada mediante mínimos cuadrados.
    """
    l_array = np.array(longitud)
    pesos_predichos = k * (l_array ** 3)
    return pesos_predichos.tolist()
    

def modelo_circ(longitudes: list[float]) -> list[float]:
    """
    longitudes: list[float] ¿Qué significa longitudes? 
    (Por favor elimina la pregunta y reemplazala con su respuesta)
    ...
    """
    ... # Puedes eliminar esta línea

def pearson(x:list[float], y: list[float]):
    """Calcula el coeficiente de pearson"""
    return float(np.corrcoef(x, y)[0, 1])


def calc_error(pred:list[float], truth: list[float]):
    """Calcula el error entre una predicción y la verdad del dataset"""


def graficar_ej2(x: list[float], y: list[float], k: float, titulo: str):
    
    # Genera la gráfica de Y = K * X
    
    x_arr = np.array(x)
    y_arr = np.array(y)
    
    plt.figure(figsize=(8, 5))
    plt.scatter(x_arr, y_arr, color='blue', label='Datos reales')
    
    #Rango para la línea continua
    x_line = np.linspace(min(x_arr)*0.9, max(x_arr)*1.1, 100)
    plt.plot(x_line, k * x_line, color='red', label=f'Ajuste: W = {k:.7f} * X')
    
    plt.title(titulo)
    plt.xlabel('Variable Independiente (X)')
    plt.ylabel('Variable Dependiente (Y)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    
    plt.show()

def main():
    ... # Puedes eliminar esta línea

if __name__ == "__main__":
    # Si necesitas hacer pruebas de tu función las puedes escribir acá
    main()

