from Trie import Trie

class MTPPhraseChecker:
    def __init__(self, words):
        self._words = words
        self._trie = Trie()
        for word in words:
            self._trie.insert(word)

    def is_valid_prefix(self, prefix):
        return self._trie.starts_with(prefix)

    def is_valid_word(self, word):
        return self._trie.search(word)