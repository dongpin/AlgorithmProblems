import unittest

from Python.BasicAlgorithm.Trie import Trie

def test_trie():
    trie = Trie()
    trie.build_trie(['add', 'new', 'slk', 'above'])
    assert trie.search('add') == True
    assert trie.search('ADD') == False
    assert trie.search('ad') == False
    assert trie.search('addd') == False
    assert trie.search('') == False
    trie.add('cup')
    assert trie.search('cup') == True