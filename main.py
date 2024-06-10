"""
This module sets up and runs the Snake game. It initializes the game screen,
creates instances of the Snake, Food, and Score classes, and manages the
game loop. The game includes functionality for controlling the snake,
detecting collisions, updating the score, and handling game over scenarios.
"""

from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

class SnakeGame:
    """A class to represent the Snake game."""

    def __init__(self):
        """Initialize the SnakeGame."""
        self.screen = Screen()
        self.setup_screen()
        self.snake = Snake()
        self.food = Food()
        self.score = Score()
        self.game_is_on = False

    def setup_screen(self):
        """Set up the game screen."""
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor('black')
        self.screen.title('Snake Game')
        self.screen.tracer(0)

    def start(self):
        """Start the Snake game."""
        self.game_is_on = True
        self.listen_to_keyboard()
        self.main_game_loop()

    def listen_to_keyboard(self):
        """Listen to keyboard inputs."""
        self.screen.listen()
        self.screen.onkey(self.snake.up, "Up")
        self.screen.onkey(self.snake.down, "Down")
        self.screen.onkey(self.snake.left, "Left")
        self.screen.onkey(self.snake.right, "Right")
        self.screen.onkey(self.reset_game, "space")

    def reset_game(self):
        """Reset the Snake game."""
        self.screen.clear()
        self.setup_screen()
        self.snake = Snake()
        self.food = Food()
        self.score = Score()
        self.start()

    def main_game_loop(self):
        """Run the main game loop."""
        while self.game_is_on:
            self.screen.update()
            time.sleep(0.1)
            self.snake.move()

            if self.snake.head.distance(self.food) < 19:
                self.food.refresh()
                self.score.increase()
                self.snake.extend()

            if (
                self.snake.head.xcor() > 280 or self.snake.head.xcor() < -280 or
                self.snake.head.ycor() > 280 or self.snake.head.ycor() < -280
            ):
                self.game_is_on = False
                self.score.game_over()

            for segment in self.snake.segments[1:]:
                if self.snake.head.distance(segment) < 10:
                    self.game_is_on = False
                    self.score.game_over()

if __name__ == "__main__":
    game = SnakeGame()
    game.start()
    Screen().exitonclick()
