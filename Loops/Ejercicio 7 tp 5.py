# 7. La función factorial se aplica a enteros positivos. El factorial de un entero positivo (!n) es igual al
# producto de todos los enteros positivos desde el 1 hasta n. Escriba un programa que calcule los
# factoriales de los enteros positivos del 1 al 5. El programa deberá mostrar la siguiente salida:
# !1 = 1
# !2 = 1*2 = 2
# ...
# !5 = 1*2*3*4*5 = 120

#Inpput: enteros del 1 al 5
#Output: factoriales con sus multiplicaciones
texto = ''
factorial = 1
for numero in range(1, 6):
    factorial = factorial * (numero)
    texto = texto + str(numero)
    texto += '*'
    print(f'{numero}! {texto}: {factorial}')

