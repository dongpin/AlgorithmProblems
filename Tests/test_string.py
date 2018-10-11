import unittest

from Python.BasicAlgorithm import String

def test_is_palindrome():
    assert String.is_palindromic('aba') == True
    assert String.is_palindromic('abbbbbbbbbbba') == True
    assert String.is_palindromic('ab') == False
    assert String.is_palindromic('') == True

def test_longest_common_subsequence():
    assert String.longest_common_subsequence('a', 'a') == 'a'
    assert String.longest_common_subsequence('ab', 'acbd') == 'ab'
    assert String.longest_common_subsequence('abcd', 'ac') == 'ac'
    assert String.longest_common_subsequence('abcdefghijk', 'caegijk') == 'aegijk'
    assert String.longest_common_subsequence('a', '') == ''
    assert String.longest_common_subsequence('', '') == ''

def test_longest_common_substring():
    assert String.longest_common_substring('OldSite:GeeksforGeeks.org', 'NewSite:GeeksQuiz.com') == 10
    assert String.longest_common_substring('abc', 'cba') == 1
    assert String.longest_common_substring('', '') == 0
