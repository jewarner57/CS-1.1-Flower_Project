from app import Flower


def test_get_turn_degrees():
    """Tests if get turn degrees gets the number of degrees needed to rotate for each petal"""
    flower = Flower(10, "red", 0, 0, 0, 0)
    flower2 = Flower(100, "red", 0, 0, 0, 0)

    assert flower.get_turn_degrees(10) == 36
    assert flower2.get_turn_degrees(100) == 3.6
