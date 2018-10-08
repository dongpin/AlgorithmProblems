import unittest

from Python.BasicAlgorithm import String

def test_is_palindrome():
    assert String.is_palindromic('aba') == True
    assert String.is_palindromic('abbbbbbbbbbba') == True
    assert String.is_palindromic('ab') == False
    assert String.is_palindromic('') == True