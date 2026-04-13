'''#definindo um coijunto usando chaves
conjunto = {1, 2, 3, 4, 5, 3, 6 , 7,11,1,2,3,4,5,6,7,8,9,10}
print(conjunto) 
#conjuntos não aceitam valores duplicados, então os valores repetidos são ignorados

n = int(input('Digite um número: '))
if n in conjunto:
    print('O número está presente no conjunto')
else:
    print('O número não está presente no conjunto')

lista = [1, 2,65,32,54,6,123,32,353,4,4,55,55,65.7,2]
novo_conjunto = set(lista)
print(novo_conjunto)

'''

banco_de_dados = []
info_pessoais = []

while True:
    cpf = int(input("informe seu cpf: "))
    email = input("informe seu email: ")
    nome = input('informe o seu nome completo: ')
    idade = input('informe a sua idade: ')
    