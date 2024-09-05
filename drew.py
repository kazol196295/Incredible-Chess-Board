
import pygame

# Setting Width and height of the Chess Game screen
WIDTH = 600
HEIGHT = 600
INF = 100000000000000000000
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS



BOARD_COLOR_1 = (238, 238, 210)
BOARD_COLOR_2 = (118, 150, 86)
WHITE_PAWN_COLOR = (255, 255, 255)
BLACK_PAWN_COLOR = (0, 0, 0)
BACKGROUND_COLOR = (0, 0, 0)


white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7)]

# white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]
# black_locations = [(0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]

val = [[0, 1, 1, 1, 1, 1, 1, 0],
       [0, 1, 1, 1, 1, 1, 1, 0],
       [0, 1, 1, 1, 1, 1, 1, 0],
       [0, 1, 1, 1, 1, 1, 1, 0],
       [0, 1, 1, 1, 1, 1, 1, 0],
       [0, 1, 1, 1, 1, 1, 1, 0],
       [0, 1, 1, 1, 1, 1, 1, 0],
       [0, 1, 1, 1, 1, 1, 1, 0]]

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Incredible Board Game')


def draw_board(turn_step):
    for row in range(ROWS):
        for col in range(COLS):
            color = BOARD_COLOR_1 if (row + col) % 2 == 0 else BOARD_COLOR_2
            pygame.draw.rect(screen, color, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# draw pieces onto board
def draw_pieces(turn_step, selection):
    for i in range(len(white_locations)):
        pygame.draw.circle(screen, WHITE_PAWN_COLOR, (white_locations[i][0] * SQUARE_SIZE + SQUARE_SIZE // 2,
         white_locations[i][1] * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 3)

        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, 'red', [white_locations[i][0] * SQUARE_SIZE + 1, white_locations[i][1] * SQUARE_SIZE + 1,
                                                 SQUARE_SIZE, SQUARE_SIZE], 2)

    for i in range(len(black_locations)):
        pygame.draw.circle(screen, BLACK_PAWN_COLOR, (black_locations[i][0] * SQUARE_SIZE + SQUARE_SIZE // 2,
        black_locations[i][1] * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 3)

        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'blue', [black_locations[i][0] * SQUARE_SIZE + 1, black_locations[i][1] * SQUARE_SIZE + 1,
                                                  SQUARE_SIZE, SQUARE_SIZE], 2)



# draw valid moves on screen
def draw_valid(moves):
    color = 'red'
    for i in range(len(moves)):
        pygame.draw.circle(
            screen, color, (moves[i][0] * SQUARE_SIZE + SQUARE_SIZE // 2, moves[i][1] * SQUARE_SIZE + SQUARE_SIZE // 2), 10)