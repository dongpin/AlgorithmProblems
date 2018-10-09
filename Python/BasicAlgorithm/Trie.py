
from collections import defaultdict

class Trie:
    def __init__(self):
        self.paths = defaultdict(Trie)
        self.word_end = False
    
    def add(self, word):
        pass
            
