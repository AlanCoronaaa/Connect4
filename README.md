---

# Connect 4

## Overview

**Connect 4** is a command-line based Python game that simulates the classic Connect 4. This project was created to enhance Python programming skills and computational thinking. The game supports both single-player (against the computer) and two-player modes, where players take turns to drop their discs into a grid with the goal of connecting four in a row, either horizontally, vertically, or diagonally.

## Features

- **Two Game Modes**: 
  - **Single-Player**: Play against a computer opponent.
  - **Two-Player**: Compete against another human player.
- **Turn-Based Gameplay**: Players alternate turns to drop their discs, with clear indications of whose turn it is.
- **Winning Logic**: Detects and announces the winner when a player aligns four discs consecutively.
- **Scoreboard**: Tracks and records wins, displaying a global leaderboard and a history of past games.
- **Data Persistence**: Saves game results and player statistics for future sessions.

## Project Structure

- **`connect4.py`**: The main game script that handles game initialization, player input, game logic, and win conditions.
- **`lib_frames_conecta4.py`** and **`Generador_matrices.py`**: Auxiliary modules that support game functionalities such as rendering the game board, managing the game state, and processing player moves.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.
- `colorama` library installed for terminal text formatting. You can install it via pip:
  ```
  pip install colorama
  ```

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/AlanCoronaaa/Connect4.git
   ```
2. Navigate to the project directory:
   ```
   cd Connect4
   ```
3. Run the game:
   ```
   python connect4.py
   ```

### How to Play

1. **Launch the Game**: Start the game by running the `connect4.py` script.
2. **Select Game Mode**: Choose between playing against another player or the computer.
3. **Take Turns**: Input the column number where you want to drop your disc.
4. **Win the Game**: Align four discs in a row, column, or diagonal to win the game.
5. **Check Leaderboards**: View the top players and game history from the main menu.

## Contributing

Contributions to enhance this project are welcome. You can fork the repository, submit issues, or create pull requests to add new features or fix bugs.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- **Colorama**: For terminal text formatting.
- Everyone who provided feedback and support during the development of this project.
