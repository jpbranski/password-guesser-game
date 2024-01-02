import pytest
from project import get_file_name, game_win, play_again


def test_get_file_name():
    assert get_file_name(1) == "words1.txt"
    assert get_file_name(5) == "words5.txt"
    assert get_file_name(3) == "words3.txt"

def test_game_win():
    assert game_win("jack", 1, 1) == "jack has beaten difficulty 1 with a score of 5000!"
    assert game_win("ailbhe", 5, 7) == "ailbhe has beaten difficulty 5 with a score of 10750!"

def test_play_again():
    assert play_again("y") == True
    assert play_again("n") == False