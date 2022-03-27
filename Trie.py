class Trie(object):
    def __init__(self):
        self.child = {}

    def insert(self, word):
        current = self.child
        for l in word:
            if l not in current:
                current[l] = {}
            current = current[l]
        current['#']=1

    def search(self, word):
        current = self.child
        for l in word:
            #print("Current:", current)
            if l not in current:
                return False
            current = current[l]
        return '#' in current

    def starts_with(self, prefix):
        current = self.child
        for l in prefix:
            if l not in current:
                return False
            current = current[l]
        return True



# https://www.tutorialspoint.com/implement-trie-prefix-tree-in-python