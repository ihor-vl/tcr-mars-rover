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


def run():
    gird_x = int(input("Enter the grid x: "))
    if gird_x < 1:
        raise ValueError("Grid x should be greater than 0")
    grid_y = int(input("Enter the grid y: "))
    if grid_y < 1:
        raise ValueError("Grid y should be greater than 0")
    grid = Grid(gird_x, grid_y)
    x = int(input("Enter the x position of the rover: "))
    if x < 1:
        raise ValueError("Rover x should be greater than 0")
    elif x > gird_x:
        raise ValueError("Rover x should be less than grid x")
    y = int(input("Enter the y position of the rover: "))
    if y < 1:
        raise ValueError("Rover y should be greater than 0")
    elif y > grid_y:
        raise ValueError("Rover y should be less than grid y")
    direction = input("Enter the direction of the rover: ")
    if direction.upper() not in ["N", "E", "S", "W"]:
        raise ValueError("Direction should be N, E, S or W")
    position = Position(x, y, direction)
    rover = Rover(grid, position)
    print(rover.state())


if __name__ == "__main__":
    run()
