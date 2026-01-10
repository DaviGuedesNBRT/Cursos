#recebendo dados do usuario atravez do terminal

print("testes recebendo dados atravez do input")

#declarando o tipo da variavel enquanto recebe o valor 
nome = str(input('informe seu nome :'))
idade = int(input('informe sua idade :'))
cpf = int(input('informe seu cpf :'))
altura = float(input('digite sua altura em metros :'))

#print mais rustico
print('Olá, {} !! sua idade: {} anos e CPF: {} '.format(nome,idade,cpf))

#teste de outro tipo de print
print(f"olá {nome}!! seua idade é {idade} anos")

#teste de eoperações no print
print(f'Olá, {nome}!!! seu ano de nascimento é {2026-idade}')

print(f"olá {nome}!! seua altura é {altura} metros")


#conversão de float para int irá arredondar o numero para baixo!!
#o int é inpreciso. para melhor precisão, ultiliza-se float
conversao = int(altura)
print(conversao)

#é possivel trabalhar com números imaginario ultilizando a tipagem "complex" ou adicionando um "j" ao numero da variavel
nc = complex(input("escreva um numero para torna-lo imaginario :"))
nc2 = 5j
print(f' sao nuemros complexos {nc} e {nc2}')

#não sei ao certo para que iria ultilizar isso, nem na escola entendia a finalidade kkkkk
