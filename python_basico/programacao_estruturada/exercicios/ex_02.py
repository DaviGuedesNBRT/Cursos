#exercicios condicionais python

#1. Faça um programa que receba dois números inteiros e mostre qual deles é o maior.
n1 = int(input("digite um numero: "))
n2 = int(input("digite um numero: "))

if n1 > n2:
    print(f'{n1} > {n2}')

else:
    print(f'{n2} > {n1}')

print('===========================')
print('===========================')

'''2. Faça um programa que leia um número inteiro fornecido pelo usuário. Se esse número for positivo, calcule 
a raiz quadrada do número e apresente-a. Se o número for negativo, mostre uma mensagem dizendo que o 
número é inválido.'''

n3 = int(input("digite um numero: "))

if n3 > 0:
    print(f'a raiz quadrada de {n3} é {n3*n3}')

else: 
    print('valor invalido')

print('===========================')
print('===========================')

'''3. Faça um programa que recebe um número inteiro e informe se este número é par ou ímpar.'''

n4 = int(input('digite um numero: '))

if n4 % 2 == 0 :
    print(f"o numero {n4} é par")

else:
    print(f"o numero {n4} é imapr")