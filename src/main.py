from typing import NamedTuple, Literal


class Grid(NamedTuple):
    x: int
    y: int


class Position(NamedTuple):
    x: int
    y: int
    direction: Literal["N", "E", "S", "W"]


class Rover:

    def __init__(self, grid: Grid, position: Position):
        self.grid = grid
        self.position = position

    def state(self) -> str:
        return f"X: {self.position.x} Y: {self.position.y}  Direction: {self.position.direction}"

    def move_forward(self) -> None:
        self.position = Position(self.position.x, self.position.y + 1, direction=self.position.direction)

    def turn_left(self) -> None:
        directions = {"N": "W", "W": "S", "S": "E", "E": "N"}
        self.position = Position(
            self.position.x,
            self.position.y,
            direction=directions[self.position.direction]
        )

    def turn_right(self) -> None:
        directions = {"N": "E", "E": "S", "S": "W", "W": "N"}
        self.position = Position(
            self.position.x,
            self.position.y,
            direction=directions[self.position.direction]
        )
