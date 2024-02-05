from src.main import Rover, Grid, Position


def test_dummy():
    assert True


def test_rover_status():
    rover = Rover(Grid(10, 10), Position(3, 7, "E"))
    assert rover.state() == "X: 3 Y: 7  Direction: E"
