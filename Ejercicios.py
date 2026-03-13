#Ejercicio 1
#La explicación de este ejercicio la pueden encontrar en README.md
from data import read_data
from main import similitud_geometrica

longitud, peso = read_data("data/pescados.csv")
similitud_geometrica(longitud, peso)
