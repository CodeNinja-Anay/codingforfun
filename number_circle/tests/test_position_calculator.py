from src.position_calculator import position_calculator

def test_position_calculator():
    items = [1, 2, 3]
    radius, positions = position_calculator(items)
    assert radius > 0
    assert len(positions) == len(items)