#!/usr/bin/python3
import sys
from enum import Enum

class Tile(Enum):
    empty = 0
    player = 1
    enemy = 2

class MoveType(Enum):
    # nothing = 0
    move = 1
    attack = 2
    barrier = 3
    # move_attack = 4
    # move_barrier = 5

def init_board(size, n_enemies):
    board = [[Tile.empty for i in range(size)] for j in range(size)]
    board[0][0] = board[1][0] = board[0][1] = Tile.player
    return board

def tile_to_string(tile):
    if tile == Tile.empty:
        return '-'
    elif tile == Tile.player:
        return 'o'
    elif tile == Tile.enemy:
        return 'x'

def print_board(board):
    print('[')
    for row in board:
        print(' '.join([tile_to_string(tile) for tile in row]))
    print(']')

def is_win(board):
    for row in board:
        for tile in row:
            if tile == Tile.enemy:
                return False
    return True

def is_loss(board):
    for row in board:
        for tile in row:
            if tile == Tile.player:
                return False
    return True

def apply_moves(board, moves):
    pass

def get_moves(board):
    """Return a list of possible moves"""
    pass

def minimax(board, depth, is_maximizing):
    if is_loss(board):
        return -1
    if is_win(board):
        return 1
# 01 function minimax(node, depth, maximizingPlayer)
# 02     if depth = 0 or node is a terminal node
# 03         return the heuristic value of node

# 04     if maximizingPlayer
# 05         bestValue := −∞
# 06         for each child of node
# 07             v := minimax(child, depth − 1, FALSE)
# 08             bestValue := max(bestValue, v)
# 09         return bestValue

# 10     else    (* minimizing player *)
# 11         bestValue := +∞
# 12         for each child of node
# 13             v := minimax(child, depth − 1, TRUE)
# 14             bestValue := min(bestValue, v)
# 15         return bestValue

def generate():
    # Repeat:
    # Generate a random game
    # Run minimax to verify the game is solvable
    # If possible, also enforce "hardness conditions"
    pass

if __name__ == '__main__':
    # TODO repl
    # repl: play against AI
    # generate()
    # r reset
    # m move r1 c1 r2 c2
    # b barrier
    # s save
    # n next
    print_board(init_board(5, 4))


