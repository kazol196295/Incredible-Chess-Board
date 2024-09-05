# Importing Modules
import pygame
from drew import *
from ai import *


from io import BytesIO

pygame.init()


winner = ''
game_over = False
turn_step = 0
selection = 100
valid_moves = []



run = True
while run:
    screen.fill('dark gray')
    draw_board(turn_step)
    draw_pieces(turn_step, selection)
    if selection != 100:
        draw_valid(valid_moves)

    # event handling
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            x_coord = event.pos[0] // SQUARE_SIZE
            y_coord = event.pos[1] // SQUARE_SIZE
            click_coords = (x_coord, y_coord)

            if turn_step <= 1:
                if click_coords in white_locations:
                    selection = white_locations.index(click_coords)
                    for y in range(y_coord, ROWS):
                        if val[x_coord][y]:
                            valid_moves.append((x_coord, y))
                    if turn_step == 0:
                        turn_step = 1
                    if len(valid_moves) == 0:
                        winner = "Black"
                        game_over = True
                if click_coords in valid_moves and selection != 100:
                    for y in range(white_locations[selection][1], y_coord + 1):
                        val[x_coord][y] = 0
                    white_locations[selection] = click_coords
                    turn_step = 2
                    selection = 100
                    valid_moves = []
        if turn_step == 2:
        #AI's turn
            eval, move = minimax(white_locations[:], black_locations[:], 1, -INF, INF)
            if move == (-1, -1):
                winner = "White"
                game_over = True
            else:
                for y in range(black_locations[move[0]][1],  move[1] - 1, -1):
                        val[move[0]][y] = 0
                black_locations[move[0]] = move
            turn_step = 1



    # print(eval, move)


   

    pygame.display.flip()

pygame.quit()