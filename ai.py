from drew import *
import random as rand

INF = 10 ** 20

# white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]
# black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (9, 7)]

def get_all_moves(white_locations, black_locations, x):
	moves = []

	for y in range(white_locations[x][1] + 1, black_locations[x][1]):
		moves.append((x, y))

	return moves


def heuristic_value(white_locations, black_locations):
	xr = 0
	for x in range(COLS):
		xr ^= (black_locations[x][1] - white_locations[x][1] - 1)
	return xr


def minimax(white_locations, black_locations, turn, alpha, beta):
	# print(val)
	# print(white_locations, black_locations, turn)
	
	if turn == 1:
		max_eval = -INF
		best_move = (-1, -1)
		for x in range(COLS):
			moves = get_all_moves(white_locations, black_locations, x)

			for move in moves:

				black_locations1 = black_locations[:]
				black_locations1[x] = move
				# print(black_locations[x][1], move[1], moves)
				# print(heuristic_value(white_locations, black_locations1), move)
				if heuristic_value(white_locations, black_locations1) == 0:

					eval, move1 = minimax(white_locations[:], black_locations1, turn ^ 1, alpha, beta)
			
					if eval >= max_eval:
						max_eval = eval
						best_move = move
					alpha = max(alpha, max_eval)

				if alpha >= beta:
					return max_eval, best_move

			if best_move == (-1, -1) and len(moves) != 0:
				best_move = moves[rand.randint(0, len(moves) - 1)]
		return max_eval, best_move
	else:
		min_eval = INF
		best_move = (-1, -1)
		for x in range(COLS):
			moves = get_all_moves(white_locations, black_locations, x)

			for move in moves:
				white_locations1 = white_locations[:]
				white_locations1[x] = move

				if heuristic_value(white_locations1, black_locations) == 0:
					eval, move1 = minimax(white_locations1, black_locations[:], turn ^ 1, alpha, beta)
					# print(white_locations[x][1], move[1], moves, eval)
			
					if eval <= min_eval:
						min_eval = eval
						best_move = move

				beta = min(beta, min_eval)
				if beta <= alpha:
					return min_eval, best_move

			if best_move == (-1, -1) and len(moves) != 0:
				best_move = moves[rand.randint(0, len(moves) - 1)]
		return min_eval, best_move

# eval, move = minimax(white_locations, black_locations, 1, -INF, INF)

# print(eval, move)