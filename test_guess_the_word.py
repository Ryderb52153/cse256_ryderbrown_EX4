# Ryder Brown
# CIS256 Fall 2024
# EX 4

import pytest
from guess_the_word import select_word, display_word

def test_select_word():
    words = ["python", "programming", "testing", "debugging", "developer"]
    word = select_word()
    assert word in words

def test_display_word():
    word = "python"
    guessed_letters = {"p", "y"}
    assert display_word(word, guessed_letters) == "p y _ _ _ _"