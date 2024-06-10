"""
This module contains the Score class used for creating and controlling
the score display in the Snake game. The Score class includes methods for 
updating the score, increasing the score, displaying the game over message,
and resetting the score.
"""

from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')

class Score(Turtle):
    """A class to represent the score display in the Snake game."""

    def __init__(self):
        """Initialize the score display."""
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.score = 0
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        """Update the score display with the current score."""
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase(self):
        """Increase the score by one and update the display."""
        self.score += 1
        self.update_score()

    def game_over(self):
        """Display the game over message in the center of the screen."""
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        self.goto(0, -30)
        self.write("Press Space to Play Again", align=ALIGNMENT, font=FONT)
