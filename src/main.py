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

    def _check_new_position(self, x, y):
        if x > self.grid.x:
            x = 1
        elif x < 1:
            x = self.grid.x

        if y > self.grid.y:
            y = 1
        elif y < 1:
            y = self.grid.y

        return x, y

    def move_forward(self) -> None:
        x, y, d = self.position
        if d == "N":
            y += 1
        elif d == "S":
            y -= 1
        elif d == "E":
            x += 1
        elif d == "W":
            x -= 1

        x, y = self._check_new_position(x, y)
        self.position = Position(x=x, y=y, direction=d)

    def move_backward(self) -> None:
        x, y, d = self.position
        if d == "N":
            y -= 1
        elif d == "S":
            y += 1
        elif d == "E":
            x -= 1
        elif d == "W":
            x += 1

        x, y = self._check_new_position(x, y)
        self.position = Position(x=x, y=y, direction=d)

    def turn_left(self) -> None:
        self.turn({"N": "W", "W": "S", "S": "E", "E": "N"})

    def turn_right(self) -> None:
        self.turn({"N": "E", "E": "S", "S": "W", "W": "N"})

    def turn(self, directions: dict):
        self.position = Position(
            self.position.x,
            self.position.y,
            direction=directions[self.position.direction]
        )

    def follow_instructions(self, instructions: str) -> None:
        for instruction in instructions:
            if instruction.upper() == "F":
                self.move_forward()
            if instruction.upper() == "B":
                self.move_backward()
            elif instruction.upper() == "L":
                self.turn_left()
            elif instruction.upper() == "R":
                self.turn_right()
            else:
                continue
