[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/jw8MUQHd)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=23098727)
# Práctica 05

Este es un archivo de ejemplo donde debes de colocar la respuesta a tus ejercicios, piénsalo como tu reporte de práctica. Aquí puedes introducir el problema y definir los términos que consideres apropiados de forma concisa.

## Integrantes

Escribe tus integrantes iniciando por apellido de forma alfabética

- (Si no modificas esta línea lloro) Segundo, Aureliano
- Sánchez Cruz Octavio Jesús
- (Si no modificas esta línea lloro) Segundo, Aureliano


## Uso e instalación

Aquí escribe qué necesitas que instale para ejecutar tu código, por ejemplo:

- `matplotlib as plt`
- `numpy as np`

Y dime cómo debería ejecutar tu código y en qué orden. Recuerda que antes de ejecutar tu código leeré tu `README.md`. Por ejemplo la manera en la que propongo que organizes tu código es

- `README.md`: Contiene las instrucciones, la discusión y la solución de cada ejercicio.
- `data.py`: Contiene al a función que lee los datos del csv.
- `main.py`: Contiene el código para calcular la relación entre peso y longitud.
- `` (Por favor modifica esta línea)
- `Ejercicios.py`: Contiene el codigo que llama a las funciones y resuelve cada uno de los ejercicios.

## Ejercicio 1

Para poder ajustar nuestro modelo necesitamos datos sobre el peso (W) y la longitud (l) de algunos pescados. Los únicos datos sobrevivientes de los campeonatos anteriores se
encuentran en la siguiente tabla:

| Longitud (cm)| Masa (kg) |
| -------- | ------------- |
| $36.81$ | $0.78$ |
| $31.77$ | $0.47$ |
| $43.82$ | $1.16$ |
| $36.82$ | $0.74$ |
| $32.07$ | $0.44$ |
| $45.07$ | $1.40$ |
| $35.89$ | $0.64$ |

En realidad, lo que medimos cuando "pesamos" en kg es la masa, y no el peso, de lo que estemos midiendo.

Bajo los supuestos: la especie está fija y todos los pescados serán robalos; la densidad de los pescados es constante; las variables como la estación del año, el sexo, la edad, etc; no afectan al peso del róbalo y los róbalos son geométricamente similares.

Por lo anterior tenemos que la densidad es constante y que hay similitud geómetrica; es decir, el crecimiento del peso es proporcional a el crecimiento de volumen del róbalo.

¿Por qué el crecimiento del peso es proporcional al crecimiento del volumen? 

*W = mg y m = dV*

De lo anterior se tiene que *W = dVg* pero como "d" y "g" son constantes, tendremos que *W = cV*

Para resolver el ejecicio daremos la ubicación de cada uno de los puntos dentro del espacio volumen-peso; posteriormente calculamos la línea recta que más se aproxima a todos los puntos y la cual nos dará la mejor aproximación hacia la gráfica que relaciona el peso con el volumen del róbalo.


## Ejercicio 2

Aquí puedes colocar la discusión del modelo, tu interpretación, el efecto de las condiciones iniciales. No tiene que ser perfecto, pero entre más casos puedas cubrir mejor

(Por favor modifica esta línea, tú puedes yo creo en ti) Puedes darle formato de **negritas**, *itálicas*, incluir texto matemático $x\approx 1, \epsilon > 0$, [enlaces](https://www.markdownguide.org/cheat-sheet/), `código`,

```python
# Esto es un ejemplo, lo puedes quitar
print("Código en bloque")
```

(Si no eliminas esta línea lloro) También puedes incluir citas

> Por favor elimina esta cita

(Si no eliminas esta línea lloro) Puedes incluir notas al pie [^1].

## Ejercicio 3

También se pueden incluir imágenes. Aunque a veces aunque se muestre localmente, no significa que se vaya a mostrar en GitHub. Por ejemplo, adjunto una imagen de una bella rosa:

![Texto alternativo, imagen de la cara de un Mr. Meeseks en fondo azul con la leyenda Existence is Pain por debajo](media/existence_is_pain.jpg)

### También puedes agregar tablas y eliminar este sub encabezado

| Elimíname | Elimíname a mí también |
| -------------- | --------------- |
| $1$ | $54$ |
| $2$ | $1000$ |

(Si no eliminas esta línea lloro) Y luego puedes comentar que con base en la tabla anterior, se ve una explosión en los valores a partir del tiempo $t=2$. 

## Conclusión

(Por favor modifica esta línea bro, es la última que tienes que modificar bro, por favor bro) Es buena práctica concluir tus prácticas. ¿Qué te llevas? ¿Sientes que fue relevante para ti? ¿Se te complicó algún aspecto? ¿Hubo algún resultado que contradijera tu intuición?
