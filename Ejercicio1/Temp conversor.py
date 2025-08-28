#De celsius a fahrenheit
#0°c= (32°f-32)*5/9

print('Conversor de celsius a fahrenheit')
valor = float(input('inserta la temperatura en celsius: '))
print(f'tu temperatura en fahrenheit es de {valor*9/5+32}')

#De fahrenheit a celsius
#0°c= (32°f-32)*5/9

print('Conversor de fahrenheit a celsius')
valor = float(input('inserta la temperatura en fahrenheit: '))
print(f'tu temperatura en celsius es de {(valor-32)*5/9}')