jogador_atual = 1
s = 'O'
grid = [0] * 9

class Jogador:
    def __init__(self, nome):
        self.nome = nome
    
    
def print_grid(grid):
    a = 0        
    for pos in range (0,9,3):
        print('   │   │')        
        for c in range(a,10):
            if c == 0 or c == 3 or c == 6:
                if grid[c] == 1:
                    p1 = 'O'
                elif grid[c] == 2:
                    p1 = 'X'
                elif grid[c] == 0:
                    p1 = pos
                print(f' {p1} ',end= '')
            elif c == 1 or c == 4 or c == 7:
                if grid[c] == 1:
                    p2 = 'O'
                elif grid[c] == 2:
                    p2 = 'X'
                elif grid[c] == 0:
                    p2 = pos + 1
                print(f'│ {p2} ',end= '')
            elif c == 2 or c == 5 or c == 8:
                if grid[c] == 1:
                    p3 = 'O'
                elif grid[c] == 2:
                    p3 = 'X'
                elif grid[c] == 0:
                    p3 = pos + 2
                print(f'│ {p3} ')
            if c == 2 or c == 5:
                a += 3
                break
        if pos == 0 or pos == 3:
            print('___│___│___')

def jogada():
    while True:
        posicao_selecionada = (input('Em qual posição deseja jogar? '))
        
        try:
            posicao_selecionada = int(posicao_selecionada)
        except ValueError:
            print('Selecione um valor numérico')
            continue

        if posicao_selecionada < 0 or posicao_selecionada > 8:
            print('Selecione um número disponível na grade')
            continue

        if grid[posicao_selecionada] != 0:
            print('Posição já ocupada! Selecione outro número.')
            continue

        return posicao_selecionada
 
def fim_do_jogo(grid):
    players = [1,2]
    for p in players:
        for i in range(3):
            if grid[3 * i] == p and grid[(3 * i) + 1] == p and grid[(3 * i) + 2] == p:
                return p
            if grid[i] == p and grid[(i + 3)] == p and grid[(i + 6)] == p:
                return p
            if (grid[0] == p and grid[4] == p and grid[8] == p) or (grid[2] == p and grid[4] == p and grid[6] == p):
                return p
        
        if 0 not in grid:
            return 0


#PROGRAMA DO JOGO


# REGISTRO DE JOGADORES
jogador1 = Jogador(input('Jogador 1 - Nome: '))
jogador2 = Jogador(input('Jogador 2 - Nome: '))

while True:
    print_grid(grid)
    if jogador_atual == 1:
        atual = jogador1.nome
    else:
        atual = jogador2.nome    
    print(f'\n Vez do jogador {atual} símbolo {s}')

    local = jogada()
    grid[local] = jogador_atual

    if fim_do_jogo(grid) == 1 or fim_do_jogo(grid) == 2:
        print_grid(grid)
        if jogador_atual == 1:
            vencedor = jogador1.nome
        else:
            vencedor = jogador2.nome
        print(f'FIM DE JOGO \n{vencedor} VENCEU!!!')
        break

    if fim_do_jogo(grid) == 0:
        print_grid(grid)
        print('FIM DE JOGO \nEMPATE!!!')
        break

    if jogador_atual == 1:
        jogador_atual = 2
        s = 'X'
    else:
        jogador_atual = 1
        s = 'O'