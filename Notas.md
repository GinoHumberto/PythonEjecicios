# Número Expresados en fracciones

Primero debemos importar el modulo:
```py
from fractions import Fraction
```
Luego ya podemos establecer nuestro numero que queremos pasar a fraccion
```py
numero = 0.2
fraccion = Fraction(numero)
print(fraccion)
```
Como este fraccion tiene un numero muy largo tanto en el denominador como el numereador (3602879701896397/18014398509481984)
Podemos solucionarlo de 2 formas:
1. Podemos pasar el numero a str de esta forma:
```py
numero = 0.2
fraccion = Fraction(str(numero))
print(fraccion)
```
2. Podemos limitar los valores del numerador y el denominador para encontrar la fraccion mas cercana, por ej:
```py
numero = 0.2
fraccion = Fraction(numero)
fraccion = fraccion.limit_denominator(2)
print(fraccion)
```


# Operadores Logicos (and, or, not)
Aquí tienes las tablas de verdad para los operadores lógicos **`and`** y **`or`** en Python:

### Tabla de verdad del operador **`and`**:

El operador **`and`** devuelve `True` si **ambas** expresiones son `True`. Si alguna es `False`, el resultado será `False`.

| `A`     | `B`     | `A and B` |
|---------|---------|-----------|
| `True`  | `True`  | `True`    |
| `True`  | `False` | `False`   |
| `False` | `True`  | `False`   |
| `False` | `False` | `False`   |

### Tabla de verdad del operador **`or`**:

El operador **`or`** devuelve `True` si **al menos una** de las expresiones es `True`. Solo será `False` si **ambas** expresiones son `False`.

| `A`     | `B`     | `A or B`  |
|---------|---------|-----------|
| `True`  | `True`  | `True`    |
| `True`  | `False` | `True`    |
| `False` | `True`  | `True`    |
| `False` | `False` | `False`   |

### Ejemplos en Python:

- **`and`**:
  ```python
  print(True and True)   # Salida: True
  print(True and False)  # Salida: False
  print(False and True)  # Salida: False
  print(False and False) # Salida: False
  ```

- **`or`**:
  ```python
  print(True or True)    # Salida: True
  print(True or False)   # Salida: True
  print(False or True)   # Salida: True
  print(False or False)  # Salida: False
  ```
El operador **`not`** en Python es un operador lógico **unario** que se utiliza para **invertir** el valor de una expresión booleana. Si la expresión es `True`, el operador **`not`** devuelve `False`, y si la expresión es `False`, devuelve `True`.

### Tabla de verdad del operador **`not`**:

| `A`     | `not A` |
|---------|---------|
| `True`  | `False` |
| `False` | `True`  |

### Ejemplo de uso:

- **`not` con valores `True` y `False`**:
  ```python
  print(not True)   # Salida: False
  print(not False)  # Salida: True
  ```

- **`not` con expresiones**:
  ```python
  a = 5
  print(not (a > 3))  # La expresión (a > 3) es True, así que not devuelve False.
  print(not (a < 3))  # La expresión (a < 3) es False, así que not devuelve True.
  ```

### Uso en condiciones:

El operador **`not`** se utiliza a menudo en estructuras de control para invertir condiciones:

```python
a = 10
if not (a < 5):
    print("a no es menor que 5")  # Esta línea se ejecutará porque la condición es invertida.
```

En este caso, el **`not`** invierte la condición `(a < 5)`, por lo que el bloque `if` se ejecuta cuando `a` no es menor que 5.


  print(f'x_value:{bool(x_value)}')

# Atajos de teclado

Para seleccionar, borrar o realizar un movimiento **por palabra** se usa control. Por ejemplo suponer que necesitamos borrar la palabra hola:

```
# Posicionamos el cursor en donde está la linea "|"
Hola| mundo
```
Y apretamos la combinación de teclas ctrl+derecha para seleccionar o crtl+backspace para borrar.

Para hacer aparecer múltiples cursores entre lineas usamos ctrl+shift+abajo/arriba y apareceran más cursores en la dirección de la flecha seleccionada.

# Como hacer suma sin usar lista:
```py
#asignamos variables:
end = 5 #Es un valor de ejemplo, donde queresmos que termine la sumatoria
suma = 0 #Es donde los valores se van a empezar a sumar
n = 1 #Es el valor donde se va a comenzar la suma

while n != end + 1:
  suma = suma + n
  n += 1 #n = 1 + n
print (suma)
```