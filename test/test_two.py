from lib.two import *

def test_correct_grammar():
    result = verify_sentence_grammar("Hello, this is a fine day.")
    assert result == True

def test_empty_string():
    result = verify_sentence_grammar("")
    assert result == False

def test_lowercase_text():
    result = verify_sentence_grammar("hello")
    assert result == False

def test_uppercase_():
    result = verify_sentence_grammar("Hello")
    assert result == False

def test_punctuation_mark():
    result = verify_sentence_grammar("hello!")
    assert result == False

def test_two_sentences():
    result = verify_sentence_grammar("Hello! How are you?")
    assert result == True

