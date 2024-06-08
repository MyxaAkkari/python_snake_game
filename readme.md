# Snake Game

This is a simple Snake Game built using Python's `turtle` module. The game consists of a snake that the player controls to eat food items that appear on the screen. The goal is to make the snake grow as long as possible without hitting the walls or its own tail.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Game Rules](#game-rules)
- [Files](#files)
- [Code Overview](#code-overview)
  - [main.py](#mainpy)
  - [snake.py](#snakepy)
  - [food.py](#foodpy)
  - [score.py](#scorepy)
- [License](#license)

## Installation

To run this Snake Game, you need to have Python installed on your system. The game uses the `turtle` module, which is included in the Python Standard Library.

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/snake-game.git
    ```
2. Navigate to the project directory:
    ```bash
    cd snake-game
    ```

## Usage

Run the following command to start the game:

```bash
python main.py
```

Use the arrow keys to control the direction of the snake.

## Game Rules

- Use the arrow keys to move the snake up, down, left, or right.
- The snake grows longer each time it eats a food item.
- The game ends if the snake collides with the walls or its own tail.
- The score increases by 1 each time the snake eats a food item.

## Files

- `main.py`: The main script that initializes the game and contains the game loop.
- `snake.py`: Contains the Snake class, which manages the snake's movement and growth.
- `food.py`: Contains the Food class, which manages the appearance and placement of food items.
- `score.py`: Contains the Score class, which manages the display and updating of the score.

## Code Overview

### main.py

The main script sets up the game window, initializes the snake, food, and score objects, and contains the game loop.

### snake.py

Defines the Snake class, which handles:

- Creating the snake with initial segments
- Moving the snake
- Changing the snake's direction based on user input
- Extending the snake when it eats food

### food.py

Defines the Food class, which handles:

- Creating the food object
- Placing the food at random positions on the screen

### score.py

Defines the Score class, which handles:

- Displaying the current score on the screen
- Updating the score when the snake eats food
- Displaying the game over message when the game ends

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

Feel free to fork this repository and make your own changes. Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

Happy Coding!
