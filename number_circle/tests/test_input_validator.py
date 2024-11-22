from unittest.mock import patch
from src.input_validator import get_valid_input

def test_get_valid_input():
    with patch('builtins.input', side_effect=['10']):
        assert get_valid_input(1, 100) == 10

    with patch('builtins.input', side_effect=['-1', '101', '50']):
        assert get_valid_input(1, 100) == 50