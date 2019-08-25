import unittest

from Python.Problems.lc2_add_two_numbers import *
from Python.Problems.lc3_longest_substring_without_repeating_chars import *
from Python.Problems.lc32_longest_valid_parentheses import *
from Python.Problems.lc56_merge_intervals import *
from Python.Problems.lc44_wildcard_matching import *

# 2


def test_add_two_nums():
    head1 = ListNode(2)
    head1.next = ListNode(4)
    head1.next.next = ListNode(3)
    head2 = ListNode(5)
    head2.next = ListNode(6)
    head2.next.next = ListNode(4)

    result = add_two_numbers(head1, head2)
    assert result.val == 7
    assert result.next.val == 0
    assert result.next.next.val == 8
    assert result.next.next.next == None

# 3


def test_longest_substr_without_repeating_chars():
    assert longest_substring_without_repeating_chars("abcabcbb") == 3
    assert longest_substring_without_repeating_chars("bbbbb") == 1
    assert longest_substring_without_repeating_chars("pwwkew") == 3

# 32


def test_longest_parentheses():
    assert find_longest_valid_parenthese(")()())") == 4

# 44


def test_wildcard_matching():
    assert is_wildcard_match("aa", "*") == True
    assert is_wildcard_match("cb", "?a") == False
    assert is_wildcard_match("adceb", "*a*b") == True
    assert is_wildcard_match("acdcb", "a*c?b") == False

# 56


def test_merge_intervals():
    assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [
        [1, 6], [8, 10], [15, 18]]
