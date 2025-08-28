'''
 Realizar un programa que pida dos números enteros positivos por teclado y muestre por pantalla el
siguiente menú:
MENU
1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Salir
Elija opción:
El usuario deberá elegir una opción y el programa deberá mostrar el resultado por pantalla y luego
volver al menú. El programa deberá ejecutarse hasta que se elija la opción 5. Tener en cuenta que si el
usuario selecciona la opción 5, en vez de salir del programa directamente, se debe mostrar el siguiente
mensaje de confirmación: ​¿Está seguro que desea salir del programa (S/N)? Si el usuario selecciona el
caracter ‘S’ se sale del programa, caso contrario se vuelve a mostrar el menú.
'''
#input: 2 numeros enteros positivos, opcion del menu.
#input: confirmacion para salir "¿Está seguro que desea salir del programa (S/N)?"
#output: resultado u opcion 5(salir)

print('Bienvenido a mi programa de calculo!!\n')

################################
#      Inicio del programa     # 
################################

first_num=int(input('a. Coloca un numero que sea entero y postitivo: '))
while first_num < 0:
    print('Asegurate que el numero sea positivo')
    first_num=int(input('Coloca un numero que sea entero y postitivo: '))
else:
    second_num=int(input('\nb. Coloca otro numero que sea entero y postitivo: '))
    while second_num < 0:
        print('Asegurate que el numero sea positivo')
        second_num=int(input('Coloca otro numero que sea entero y postitivo: '))

#################
#      Menu     # 
#################

welcome=('\nBienvenido al menu, aqui vamos a calcular tus 2 numeros enteros positivos')
menu=('''\n|-----------------------|
|         Menu          |
|1.  Sumar              |
|2.  Restar             |
|3.  Multiplicar        |
|4.  Dividir            |
|5.  Salir              |
|-----------------------|''')


loop = 0 

while loop == 0:
    choice=int(input('elija la opcion: '))
    print(welcome,menu)
    if choice == 1:
        print(f'La suma de tus valores es de {first_num+second_num}')
    elif choice == 2:
        print(f'La resta de tus valores es de {first_num-second_num}')
    elif choice == 3:
        print(f'La multiplicacion de tus valores es de {first_num*second_num}')
    elif choice == 4:
        print(f'La suma de tus valores es de {first_num/second_num}')
    elif choice == 5:
        confirmation=input('¿Estas seguro que quieres salir del programa?[N/s] ')
        if confirmation == 'S' or confirmation == 'Si' or confirmation == 'si' or confirmation == 's':
            loop = 1
    else:
        print('sos webon, elegi un numero del menu, panflin.')

