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
loops = int(input("numeros de loops: "))
#posso usar isso tambem para saber o valor de um numero fatorial ex: 19!
soma = 0

for i in range(1, loops+1):
    soma += i

#meio bagunçado, mas tá bom
print(f'a quandide de loops: {loops} me fatorial é :{soma}')

print("==================")

#tabela do jogo da velha funcional

grid = [' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ']

for index in range(0,9):
    if index == 2 or index == 5 :
        print(grid[index])
        print(" ")
    else:
        print(grid[index], end="")

