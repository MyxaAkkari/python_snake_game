"""
This module contains the Snake class used for creating and controlling
a snake in the Snake game. The Snake class includes methods for moving
the snake, changing its direction, and extending its length.
"""

from turtle import Turtle

# Constants
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """A class to represent a snake in the game."""

    def __init__(self):
        """Initialize the snake."""
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Create the initial snake with predefined positions."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Add a new segment to the snake at the specified position.

        Args:
            position (tuple): The (x, y) coordinates for the new segment.
        """
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Extend the snake by adding a new segment at the last segment's position."""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Move the snake forward by moving each segment to the position of the previous segment."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Change the direction of the snake to up if it is not currently moving down."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Change the direction of the snake to down if it is not currently moving up."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Change the direction of the snake to left if it is not currently moving right."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Change the direction of the snake to right if it is not currently moving left."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset_snake(self):
        """Reset the snake to its initial state."""
        self.segments = []
        self.create_snake()
