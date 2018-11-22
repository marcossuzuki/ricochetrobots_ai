 #-*- coding: utf-8 -*-
import model

'''A partir daqui implemento a Inteligencia Artificial'''
def solve(game):
    max_depth = 1
    while 1:
        print 'Buscando profundiade: ', max_depth
        result = _search(game, [], dict(), 0, max_depth)
        if result is not None:
            return result
        max_depth += 1
        if max_depth > 30:
            return

def _search(game, path, history, depth, max_depth):
    if game.over():
        return list(path)
    
    if depth == max_depth:  #passou da profundidade
        return None

    #game.key() fornece posição dos robôs no tabuleiro formato (34, 73, 7, 58)
    #state = (depth, game.key()) #busca completa, solução ótima, processamento mais lento maior consumo de memória
    state = ''.join(map(str, game.key()))   #primeira solução viável, processamento mais rápido menor consumo de memória
    if state in history: #verifica estados repetidos
        if(len(history[state])<path):
            path = history[state]
        return None
    history.update({state:path})
    
    moves = game.get_moves(['R','G','B','Y'])  #todos movimentos possíveis

    for move in moves:
        data = game.do_move(move[0], move[1]) #game.do_move(*move) ou game.do_move(color, direction)
        path.append(move)
        result = _search(game, path, history, depth + 1, max_depth)
        path.pop(-1)
        game.undo_move(data)
        if result:
            return result
    
    return None

'''Fim da implementação da Inteligência Artificial'''