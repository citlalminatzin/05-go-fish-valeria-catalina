#!/usr/bin/env python

import numpy as np

def read_data(path="data/pescados.csv"):
    """Lee los datos de un csv y devuelve longitud y peso"""
    datos = np.genfromtxt(path, delimiter=",", skip_header=1)
    
    longitud = datos[:, 0]
    peso = datos[:, 1]
    
    return longitud, peso



