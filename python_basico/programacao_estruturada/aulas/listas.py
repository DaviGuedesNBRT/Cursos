#listas python

#odeio revisar isso tudo!!!

import random

lista = list(range(11))
print (lista)

lista_aleatoria = [random.randint(0, 10000) for i in range(10000)]

#metodo sort() organiza a lista, isso é bem util, mas pode dar um baita de um problema
lista_aleatoria.sort()

#encontrar valor em lista (19 é um exemplo)
if 19 in lista_aleatoria:
    print(f'encontrei o numero 19, {lista_aleatoria.count(19)} vezes')
    #metodo count como o nome já diz, ele conta o numero de ocorrencias :)

    # o metodo index mostra o indice onde está o valor buscado
    print(lista_aleatoria.index(19))

    #para retonar todos os indices que aparece algum valor tem quer fazer tudo isso (emoji de suspiro)
    indices = []
    for i, x in enumerate(lista_aleatoria):
        if x == 19 :
            # metodo append adiciona valor à lista, um elemento pro vez
            indices.append(i)
            #eu posso adicionar varios de uma vez ultilizando o metod extend()

            #lista.extend[123, 456, 789] dessa forma, vai adicionar cada valor individualmente 

    print(indices)


