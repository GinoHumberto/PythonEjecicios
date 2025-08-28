####################################
#       Se ejecutan n veces        #
####################################

# Este tipo de loops es util cuando se conoce la cantidad de iteraciones
# que se necesitan. 

# Por ejemplo, supongamos en en una clase se tienen 15 alumnos y a cada 
# uno de ellos se les quiere preguntar la edad y guardarla en una lista
# entonces el for es un candidato ideal para realizar esta tarea

# Porque el for itera tantas veces como le digamos. En este caso serían
# 15 veces.

edades = []
for i in range(15):
    edad = int(input(f'Edad del alumno N{i}: '))
    edades.append(edad)

# Otro ejemplo
# Supongamos que tenemos una lista de alumnos, y queremos anotar la edad
# de cada uno preguntando la edad de {nombre}:

alumnos = ['migel', 'juan', 'pepe', 'hongo']

# Estos dos bloques de codigo hacen lo mismo.

for i in range(len(alumnos)):
    alumno = alumnos[i]
    edad = int(input(f'Edad del alumno {alumno}: '))
    edades.append(edad)

for alumno in alumnos:
    edad = int(input(f'Edad del alumno {alumno}: '))
    edades.append(edad)

# Ejemplo de for hecho en while
i = 0
end_flag = len(alumnos) - 1
while i <= end_flag:
    alumno = alumnos[i]
    edad = int(input(f'Edad del alumno {alumno}: '))
    edades.append(edad)
    i += 1 # Es igual a i = i + 1

######################################################
#       No se sabe cuantas ejecuciones tendrá        #
######################################################

# Queremos obtener la edad de un usuario, y debemos
# sanitizar el input del usuario

age = int(input('Escribe tu edad: '))
while 18 > age or age > 110:
    age = int(input('Edad erronea, debe ser un numero entero entre 18 y 110'))