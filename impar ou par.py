# Sistema de informação capaz de diferenciar números impares e pares

#Apresentação
print('\n\t\t\t -- Par ou Impar -- \n')

x = int(input('informe o número: '))

if x % 2 == 0:
    print(f'\n{x} é par.')
else:
    print(f'\n{x} é impar.')