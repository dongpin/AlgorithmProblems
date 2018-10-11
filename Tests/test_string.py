import unittest

from Python.BasicAlgorithm import String

def test_is_palindrome():
    assert String.is_palindromic('aba') == True
    assert String.is_palindromic('abbbbbbbbbbba') == True
    assert String.is_palindromic('ab') == False
    assert String.is_palindromic('') == True

def test_lcs():
    assert String.lcs('a', 'a') == 'a'
    assert String.lcs('ab', 'acbd') == 'ab'
    assert String.lcs('abcd', 'ac') == 'ac'
    assert String.lcs('abcdefghijk', 'caegijk') == 'aegijk'
    assert String.lcs('a', '') == ''
    assert String.lcs('', '') == ''