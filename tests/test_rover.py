import pytest
from src.main import Rover, Grid, Position


def test_dummy():
    assert True


def test_rover_status():
    rover = Rover(Grid(10, 10), Position(3, 7, "E"))
    assert rover.state() == "X: 3 Y: 7  Direction: E"


def test_move_forward():
    rover = Rover(Grid(10, 10), Position(3, 7, "N"))
    rover.move_forward()
    assert rover.position.x == 3
    assert rover.position.y == 8
    assert rover.position.direction == "N"


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
