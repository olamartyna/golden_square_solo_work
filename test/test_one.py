from lib.one import *
import pytest

"""
Given a string with 200 words
It returns 1 minute
"""

text = "Good morning. What is the time now in Eastern Europe? "
# text contains 10 words 

def test_count_200_words():
    result = estimate_reading_time(text * 20)
    assert result == 1


"""
Given a string containing 400 words
It returns 2 minutes
"""
def test_count_400_words():
    result = estimate_reading_time(text * 40)
    assert result == 2

"""
Given a string containing 1600 words
It returns 8 minutes
"""
def test_count_1600_words():
    result = estimate_reading_time(text * 160)
    assert result == 8

"""
Given a string containing less than 200 words, e.g. 100
It returns: reading time below 1 minute
"""
def test_count_100_words():
    result = estimate_reading_time(text * 10)
    assert result == 0.5

"""
Given an empty text
It will rasie an error
"""
def test_empty_string():
    with pytest.raises(Exception) as e:
        estimate_reading_time("")
    error_message = str(e.value)
    assert error_message == "Can't estimate reading time of an empty text"
