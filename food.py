"""
This module contains the Food class used for creating and controlling
the food in the Snake game. The Food class includes methods for 
initializing the food and refreshing its position.
"""

from turtle import Turtle
from random import randint

class Food(Turtle):
    """A class to represent the food in the Snake game."""

    def __init__(self):
        """Initialize the food."""
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.color('red')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        """Refresh the food's position to a random location on the screen."""
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(random_x, random_y)
