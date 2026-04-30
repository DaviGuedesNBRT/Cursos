# Jogo da velha no terminal

rodadas = 0
nome_jogador1 = input("Informe o nome do jogador 1: ")
nome_jogador2 = input("Informe o nome do jogador 2: ")

# Padronizei os espaços para facilitar a comparação
grid = [' [0] ', ' [1] ', ' [2] ', ' [3] ', ' [4] ', ' [5] ', ' [6] ', ' [7] ', ' [8] ']

def print_grid(grid):
    print("\n")
    for index in range(0, 9):
        if index in [2, 5, 8]:
            print(grid[index])
        else:
            print(grid[index], end="")
    print("\n")

def verifica_grid(grid):
    vitorias = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # linhas
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # colunas
        (0, 4, 8), (2, 4, 6)             # diagonais
    ]

    for a, b, c in vitorias:
        # Removi os espaços extras na comparação para bater com o que é atribuído
        if grid[a] == grid[b] == grid[c] == "  X  ":
            return 1
        elif grid[a] == grid[b] == grid[c] == "  O  ":
            return 2
    return 0

# Loop principal
while True:
    print_grid(grid)
    
    # --- JOGADOR 1 ---
    escolha1 = int(input(f"{nome_jogador1}, informe o local da jogada (X): "))
    
    # Loop de validação: enquanto o lugar estiver ocupado, pede de novo
    while grid[escolha1] == "  X  " or grid[escolha1] == "  O  ":
        escolha1 = int(input(f"LOCAL OCUPADO! {nome_jogador1}, escolha outro lugar: "))
    
    grid[escolha1] = "  X  "
    rodadas += 1
    
    if verifica_grid(grid) == 1:
        print_grid(grid)
        print(f'Parabéns {nome_jogador1}, você ganhou!!')
        break
    
    if rodadas == 9:
        print_grid(grid)
        print("Empate!")
        break

    print_grid(grid)

    # --- JOGADOR 2 ---
    escolha2 = int(input(f"{nome_jogador2}, informe o local da jogada (O): "))
    
    while grid[escolha2] == "  X  " or grid[escolha2] == "  O  ":
        escolha2 = int(input(f"LOCAL OCUPADO! {nome_jogador2}, escolha outro lugar: "))
    
    grid[escolha2] = "  O  "
    rodadas += 1

    if verifica_grid(grid) == 2:
        print_grid(grid)
        print(f'Parabéns {nome_jogador2}, você ganhou!!')
        break