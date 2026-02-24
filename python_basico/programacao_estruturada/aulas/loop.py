#estru'turas de repetição python 

nome = "davi guedes noberto"
lista = [4,6,7,9,2,5,7,1,3,6]

#pecorrendo string
for letra in nome:
    #usar parametro "end" para nao pular linhas
    #se o end estiver com espaços, vai ter espoçaos a cada print
    print(letra, end="")
    print("")

print("==================")

#pecorrendo lista
for n in lista:
    print(n)

print("==================")

#loop padrão (valor inicial é 0 e o final é ignorado)
for i in range(0,10):
    print(i)

print("==================")

#posso usar variaveis para definir a quantidade de loops
loops = int(input("digite um numero que você quer saber o fatorial: "))
#posso usar isso tambem para saber o valor de um numero fatorial ex: 19!
soma = 0

for i in range(1, loops+1):
    soma += i

#meio bagunçado, mas tá bom
print(f'a quandide de loops: {loops} me fatorial é :{soma}')

print("==================")


#loop while 

numero = int(input("digite um numero maior que 100 :"))

# a estrutura while é um if com repetiçao
while numero < 100:
    print("o numero digitado é menor que 100")
    numero = int(input("digite um numero maior que 100 :"))

    decisao = input('desejan interromper ? [S/N] :')
    #posso quebrar a repetição usando brake

    if decisao[0].upper() == "S" :
        break
