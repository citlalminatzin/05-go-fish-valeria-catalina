#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
"""¿Eliminamos lo siguiente?
from models import calc_error, modelo_geom, modelo_circ
"""

def similtud_geometrica(longitud : list[float],  masa : list[float]):
    longitud = np.array(longitud)
    peso = np.array(masa)*9.81
    
    l_prom = np.mean(longitud)
    w_prom = np.mean(peso)

    m = np.sum((longitud - l_prom)*(peso - w_prom)) / np.sum((longitud - l_prom)**2)
    b = w_prom - m*l_prom

    x = np.linspace(min(longitud), max(longitud), 100)
    y = m*x + b

    plt.scatter(longitud, peso, label="Datos")
    plt.plot(x, y, label=f"Recta promedio: W = {m:.3f}l + {b:.3f}")

    plt.xlabel("Longitud")
    plt.ylabel("Peso")
    plt.title("Relación Longitud vs Peso")
    plt.legend()
    plt.grid()
    plt.show()

    return m, b
def main():
    """
    (Si no modificas esta cadena de texto lloro)
    Aquí va el código, recuerda reutilizar el 
    código que ya escribiste en otros archivos
    """
    ... # Esto significa implementación pendiente, lo puedes eliminar

if __name__ == "__main__":
    main()
