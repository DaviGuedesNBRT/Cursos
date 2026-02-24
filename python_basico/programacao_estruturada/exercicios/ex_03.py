#1. Faça um programa que determine e mostre os cinco primeiros múltiplos de 3, considerando números maiores que 0.

multiplos = []
numeros = 0

while True:
    numeros += 1
    if numeros %3 == 0:
        multiplos.append(numeros)
    
    if len(multiplos) == 5:
        break

print(multiplos)

'''2. Faça um programa que utilize o comando while para mostrar na tela uma contagem regressiva, 
iniciando em 10 e terminando em 0. Mostre também uma mensagem “FIM!” após a contagem.
'''

contagem = 10

while contagem > 0:
    print (contagem)
    contagem -= 1
    
'''3. Faça um programa que declare um inteiro, inicialize-o com 0, incremente-o de 1000 em 1000, imprimindo 
seu valor na tela, até que seu valor seja 100000 (cem mil)'''

inteiro = 0

while inteiro != 100000:
    inteiro += 1000
    print(inteiro)