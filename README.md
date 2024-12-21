# Incredible Chess Board

Welcome to the Incredible Chess Board project! This project implements a chess engine using the minimax algorithm with alpha-beta pruning. The repository contains the implementation of the chess AI and a report on the project.

## Files in the Repository

### `ai.py`

This file contains the main implementation of the chess AI. The key functions are:

- `get_all_moves(white_locations, black_locations, x)`: Generates all possible moves for a piece located at position `x`.
- `heuristic_value(white_locations, black_locations)`: Calculates the heuristic value of the board state.
- `minimax(white_locations, black_locations, turn, alpha, beta)`: Implements the minimax algorithm with alpha-beta pruning to determine the best move.

### `Report AI project .pdf`

This is a detailed report on the AI project, explaining the design, implementation, and results of the chess engine.

## How to Run

1. Clone the repository:
   ```sh
    git clone https://github.com/kazol196295/Incredible-Chess-Board.git
    cd Incredible-Chess-Board
    python ai.py


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Special thanks to the university for providing the resources and guidance for this project.
