#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
"""¿Eliminamos lo siguiente?
from models import calc_error, modelo_geom, modelo_circ
"""

def similitud_geometrica(longitud : list[float],  masa : list[float]):
    """Calcula la constante K para el modelo W = K * l^3 usando Mínimos Cuadrados."""
    
    # Convertimos las listas a arreglos de numpy
    l_array = np.array(longitud)
    w_array = np.array(masa)
    
    # Transformamos nuestra variable independiente (longitud al cubo)
    x = l_array ** 3
    
    # Calculamos la constante K (x = l^3, y = masa)
    K = np.sum(x * w_array) / np.sum(x ** 2)
    
    return float(K)

def main():
    """
    (Si no modificas esta cadena de texto lloro)
    Aquí va el código, recuerda reutilizar el 
    código que ya escribiste en otros archivos
    """
    ... # Esto significa implementación pendiente, lo puedes eliminar

if __name__ == "__main__":
    main()
