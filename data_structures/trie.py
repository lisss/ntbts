# TODO: implement this version:
# https://leetcode.com/problems/design-add-and-search-words-data-structure/


class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word: str):
        index = 0

        def _do_insert(trie, index):
            if index == len(word):
                return trie
            ch = word[index]
            next_tree = trie[ch] if ch in trie else {}
            if index == len(word) - 1:
                next_tree['is_end'] = True
            index += 1
            trie[ch] = _do_insert(next_tree, index)
            return trie
        _do_insert(self.trie, index)

    def search(self, word: str):
        """
        Returns if the word is in the trie.
        """
        index = 0

        def _do_search_exact(trie, index):
            if index == len(word):
                return False
            ch = word[index]
            if ch not in trie:
                return False
            if trie[ch].get('is_end') and index == len(word) - 1:
                return True
            index += 1
            return _do_search_exact(trie[ch], index)

        return _do_search_exact(self.trie, index)

    def startsWith(self, prefix: str):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        """
        index = 0

        def _do_search_starts_with(trie, index):
            if index == len(prefix):
                return True
            ch = prefix[index]
            if ch not in trie:
                return False
            index += 1
            return _do_search_starts_with(trie[ch], index)

        return _do_search_starts_with(self.trie, index)


print('-- case 1 --')
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))  # true
print(trie.search("app"))  # false
print(trie.startsWith("app"))  # true
trie.insert("app")
print(trie.search("app"))  # true
print(trie.search("ap"))  # false
print(trie.startsWith("ap"))  # true

print('\n-- case 2 --')
trie = Trie()
trie.insert("hello")
print(trie.search("hell"))  # false
print(trie.search("helloa"))  # false
print(trie.search("hello"))  # true
print(trie.startsWith("hell"))  # true
print(trie.startsWith("helloa"))  # false
print(trie.startsWith("hello"))  # true

print('\n-- case 3 --')
trie = Trie()
trie.insert("app")
trie.insert("apple")
trie.insert("beer")
trie.insert("add")
trie.insert("jam")
trie.insert("rental")
print(trie.search('apps'))  # false
print(trie.search('app'))  # true
print(trie.search('ad'))  # false
print(trie.search('applepie'))  # false
print(trie.search('rest'))  # false
print(trie.search('jan'))  # false
print(trie.search('rent'))  # false
print(trie.search('beer'))  # true
print(trie.search('jam'))  # true
print(trie.startsWith('apps'))  # false
print(trie.startsWith('app'))  # true
print(trie.startsWith('ad'))  # true
print(trie.startsWith('applepie'))  # false
print(trie.startsWith('rest'))  # false
print(trie.startsWith('jan'))  # false
print(trie.startsWith('rent'))  # true
print(trie.startsWith('beer'))  # true
print(trie.startsWith('jam'))  # true

print('\n-- case 4 --')
trie = Trie()
trie.insert("forefit")
trie.insert("forefinger")
print(trie.search('forefin'))  # false
