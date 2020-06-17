# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 09:41:04 2020

@author: Jonas
"""
from random import randint
from IPython.display import clear_output
print('Bem vindo ao jogo da velha!')

def display_board(board):
    clear_output()
    print ('   |   |   |')
    print (' ' + board[7]+ ' | ' + board[8]+ ' | ' + board[9])
    print ('   |   |   |')
    print ('---------------')
    print ('   |   |   |')
    print (' ' + board[4]+ ' | ' + board[5]+ ' | ' + board[6])
    print ('   |   |   |')
    print ('---------------')
    print ('   |   |   |')
    print (' ' + board[1]+ ' | ' + board[2]+ ' | ' + board[3])
    print ('   |   |   |')

def player_input():
    marker = input ("Escolha X ou O:").upper()
    while marker != 'X' and marker != 'O':
        marker = input ("digite X ou O:")
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board,mark):
    return (board[7] == mark and board[8] == mark and board [9] == mark or
            board[4] == mark and board[5] == mark and board [6] == mark or
            board[1] == mark and board[2] == mark and board [3] == mark or
            board[1] == mark and board[5] == mark and board [9] == mark or
            board[7] == mark and board[5] == mark and board [3] == mark or
            board[1] == mark and board[4] == mark and board [7] == mark or
            board[2] == mark and board[5] == mark and board [8] == mark or
            board[3] == mark and board[6] == mark and board [9] == mark
            )

def choose_first():
    print("Player:", randint(1,2),"começa")
    
def space_check(board, position):
    return (board[position] == ' ')

def full_board_check(board):
    return ((board[1] == 'X' or board[1] == 'O') and
            (board[2] == 'X' or board[2] == 'O') and
            (board[3] == 'X' or board[3] == 'O') and
            (board[4] == 'X' or board[4] == 'O') and
            (board[5] == 'X' or board[5] == 'O') and
            (board[6] == 'X' or board[6] == 'O') and
            (board[7] == 'X' or board[7] == 'O') and
            (board[8] == 'X' or board[8] == 'O') and
            (board[9] == 'X' or board[9] == 'O'))

def player_choice(board):
    position = int(input("digite uma posição (1 a 9):"))
    space_check(board, position)
    if space_check == True:
        return (position)
    else:
        position = int(input("digite outra posição (1 a 9):"))
        space_check(board, position)
        
def replay():
    jogar_novamente = input ("Vocês querem jogar novamente?, digite Sim ou Nao:")
    return (jogar_novamente == "Sim")


while True:
    board = ['X', ' ',' ',' ',' ',' ',' ',' ',' ',' ']
    # Defina o jogo
    if choose_first():
        print("O jogo vai começar")
    display_board(board)
    mark = player_input()
    game_on = win_check(board,mark[0]) or win_check(board,mark[1])
    posicoes = full_board_check(board)
    while game_on == False and posicoes == False:
        # Vez do jogador 1
        position = int(input("Digite uma posição:"))
        while space_check(board, position) == False:
            position = int(input("Digite outra posição:"))
        marker = mark[0]
        place_marker(board, marker, position)
        display_board(board)  
        game_on = win_check(board,mark[0]) or win_check(board,mark[1])
        posicoes = full_board_check(board)
        if game_on:
            print("jogador 1 ganhou")
            break
        elif posicoes:
            print("o jogo acabou")
            break
        # Vez do jogador 2
        position = int(input("Digite uma posição:"))
        while space_check(board, position) == False:
            position = int(input("Digite outra posição:"))
        marker = mark[1]
        place_marker(board, marker, position)
        display_board(board)
        game_on = win_check(board,mark[0]) or win_check(board,mark[1])
        posicoes = full_board_check(board)
        if game_on:
            print("jogador 2 ganhou")
            break
        elif posicoes:
            print("o jogo acabou")
            break
    if not replay():
        break