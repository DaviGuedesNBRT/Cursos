#jogo da velha no terminal

#numero de rodadas, se chegar em 9 rodadas e não houver um vencedor, é considerado empate 
rodadas = 0
nome_jogador1 = str(input("informe o nome do jogador 1 : "))
print(" ")
nome_jogador2 = str(input("informe o nome do jogador 2 : "))

grid = [' [0] ',' [1] ',' [2] ',' [3] ',' [4] ',' [5] ',' [6] ',' [7] ',' [8] ']

#função para exibir o grid na tela 
def print_grid(grid):
    for index in range(0,9):
        if index == 2 or index == 5 :
            print(grid[index])
            print(" ")
        else:
            print(grid[index], end="")
    print(" ")
    print(" ")

#função para verificar se há um vencedor
def verifica_grid(grid):
    vitorias = [
        # linhas
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        # colunas
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        # diagonais
        (0, 4, 8),
        (2, 4, 6),
    ]

    for a, b, c in vitorias:
        if grid[a] == grid[b] == grid[c] == "  X  ":
            return 1
        elif grid[a] == grid[b] == grid[c] == "  O  ":
            return 2

    return 0  # ninguém venceu

while True:
    if rodadas == 0:
        print_grid(grid)

    jogador1 = int(input(f"{nome_jogador1}, informe o local da jogada :"))

    #se o local já foi escolhido, não poderá ser escolhido novamente ou por outro jogador.
    if grid[jogador1] == "  X  " or grid[jogador1] == "  O  ":
        jogador1 = int(input(f"{nome_jogador1}, este local já esta marcado. por favor informe um novo local da jogada :"))
        grid[jogador1] = "  X  "
    
    else:
        grid[jogador1] = "  X  "

    rodadas += 1

    print_grid(grid)
    print(" ")

    if verifica_grid(grid) == 1 and rodadas < 9:
        print(f'parabens {nome_jogador1} você ganhou !!')
        break

#aqui o numero de rodadas chega a nove
    elif rodadas == 9:
        print("empate")

    jogador2 = int(input(f"{nome_jogador2}, informe o local da jogada :"))

    if grid[jogador2] == "  X  " or grid[jogador2] == "  O  ":
        jogador2 = int(input(f"{nome_jogador2}, este local já esta marcado. por favor informe um novo local da jogada :"))
        grid[jogador2] = "  O  "
    
    else:
        grid[jogador2] = "  O  "

    if verifica_grid(grid) == 2:
        print(f'parabens {nome_jogador2} você ganhou !!')
        break

    print_grid(grid)
    print(" ")
