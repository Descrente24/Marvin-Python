'''
Calcule de acordo com o que deseja
'''
import math

N1 = float(input('Digite o valor desejado para N1: \n'))
N2 = float(input('Digite o valor desejado para N2: \n'))
N3 = float(input('Digite o valor desejado para N3: \n'))

media = (N1+N2+N3)/3,
pi= 3.14,


print('1- Faça um algoritmo para ler dois números e imprimir a soma dos números lidos. \n')
print('2-Faça um algoritmo para ler três números e imprimir a soma, média e produto dos números lidos. \n')
print('3-Faça um algoritmo para ler dois números e imprimir o maior, o menor ou então dizer se são iguais. \n')
print('4-Faça um algoritmo para ler um número inteiro e dizer se o número lido é par ou impar. \n')
print('5-Faça um algoritmo para ler dois números A e B e dizer se A é divisível por B. \n')
print('6-Faça um algoritmo para ler dois números e imprimi-los em ordem crescente. \n')
print('7-Faça um algoritmo para ler três números e imprimir o maior. \n')
print('8-Faça um algoritmo para ler três números e imprimir se estes podem ou não formar um triângulo. \n '
      'Observação – Para formar os lados de um triângulo cada um dos valores tem que ser menor que a soma dos outros dois. \n')
print('9-Faça um algoritmo para ler três números e se estes poderem formar um triângulo dizer se o triângulo é “EQUILÁTERO”, “ISÓSCELES” OU “ESCALENO”. \n')
print('10-Faça um algoritmo para ler o preço de compra de uma mercadoria e calcular o seu preço de venda para que possa ser obtido um lucro de 30%. \n')
print('11-Faça um algoritmo para ler os catetos de um triângulo retângulo e calcular e imprimir a sua hipotenusa. \n') 
print('12-Faça um algoritmo para ler o raio e calcular o comprimento, a área e o volume de uma esfera. \n')   
Escolha= input('Digite o que deseja saber: ')
 
if Escolha == '1':
    soma = N1 + N2
    print(f'A soma de {N1} e {N2} é {soma}.')
    
elif Escolha == '2':
    soma = N1 + N2 + N3
    media = (N1 + N2 + N3) / 3
    produto = N1 * N2 * N3
    print(f'A soma de {N1}, {N2} e {N3} é {soma}.')
    print(f'A média dos três valores é {media}.')
    print(f'O produto dos três valores é {produto}.')
    
elif Escolha == '3':
    if N1 == N2 == N3:
        print(f'Os três números são iguais: {N1}')
    else:
        # Ordena os números em ordem decrescente
        numeros = [N1, N2, N3]
        numeros.sort(reverse=True)
        print(f'Os números em ordem decrescente são: {numeros[0]}, {numeros[1]}, {numeros[2]}')

elif Escolha == '4':
    if N1 % 2 == 0:
        print(f'O número {N1} é par.')
    else:
        print(f'O número {N1} é ímpar.')

elif Escolha == '5':
    dividir = N1/N2
    if N1 % N2 == 0:
        print(f'O número {N1} é divisivel por N2.')
    else:
        print(f'O número {N1} não é divisivel por N2.')

elif Escolha == '6':
    if N1>N2:
        print(f'Os números em ordem Crescente são: {N1}, {N2},')
    else:
        print(f'Os números em ordem Crescente são: {N2}, {N1},')

elif Escolha == '7':
    numeros = [N1, N2, N3]
    print(max(numeros))

elif Escolha == '8':
    if (N1+N2 > N3) or (N2+N3 > N1) or (N1+N3 > N2):
        print(f'Os números são capazes de formarem um triângulo')
    else:
        print(f'Os números não são capazes de formarem um triângulo')
        


