#El número de combinaciones de m elementos tomados de n es:(m/n) = (m! / n!(m-n))
#Diseñar una función que permita calcular el número combinatorio

def factorial(numero):
    ingreso = numero
    iteracion = 0
    factorial = 1
    while iteracion < ingreso + iteracion:
        factorial = ingreso * factorial
        ingreso -= 1
        iteracion += 1
    return(factorial)

def numero_combinatorio(m,n):
    m_factorial = factorial(m)
    n_factorial = factorial(n)
    resultado = (m_factorial / (n_factorial*(m-n)))
    return(resultado)

m = 5
n = 2
print(f'El numero combinatorio de m = {m} y n = {n} es {numero_combinatorio(m, n)}')


