import pytest
from src.main import Rover, Grid, Position


def test_dummy():
    assert True


def test_rover_status():
    rover = Rover(Grid(10, 10), Position(3, 7, "E"))
    assert rover.state() == "X: 3 Y: 7  Direction: E"


@pytest.mark.parametrize(
    'starting_position, final_position',
    [
        (Position(3, 7, "N"), Position(3, 8, "N")),
        (Position(3, 7, "S"), Position(3, 6, "S")),
        (Position(3, 7, "E"), Position(4, 7, "E")),
        (Position(3, 7, "W"), Position(2, 7, "W")),
    ],
)
def test_move_forward(starting_position: Position, final_position: Position):
    rover = Rover(Grid(10, 10), starting_position)
    rover.move_forward()
    assert rover.position == final_position


@pytest.mark.parametrize(
    'starting_position, final_position',
    [
        (Position(3, 7, "N"), Position(3, 6, "N")),
        (Position(3, 7, "S"), Position(3, 8, "S")),
        (Position(3, 7, "E"), Position(2, 7, "E")),
        (Position(3, 7, "W"), Position(4, 7, "W")),
    ],
)
def test_move_backward(starting_position: Position, final_position: Position):
    rover = Rover(Grid(10, 10), starting_position)
    rover.move_backward()
    assert rover.position == final_position


@pytest.mark.parametrize(
    'starting_direction, final_direction',
    [
        ("N", "W"),
        ("W", "S"),
        ("S", "E"),
        ("E", "N"),
    ],
)
def test_turn_left(starting_direction, final_direction):
    rover = Rover(Grid(10, 10), Position(3, 7, starting_direction))
    rover.turn_left()
    assert rover.position.x == 3
    assert rover.position.y == 7
    assert rover.position.direction == final_direction


@pytest.mark.parametrize(
    'starting_direction, final_direction',
    [
        ("N", "E"),
        ("E", "S"),
        ("S", "W"),
        ("W", "N"),
    ],
)
def test_turn_right(starting_direction, final_direction):
    rover = Rover(Grid(10, 10), Position(3, 7, starting_direction))
    rover.turn_right()
    assert rover.position.x == 3
    assert rover.position.y == 7
    assert rover.position.direction == final_direction
