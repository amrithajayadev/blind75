class TrieNode:
    def __init__(self):
        self.children = {}
        self.last_char = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.last_char = True

    def search(self, word: str) -> bool:
        def dfs(j, node):
            cur = node
            for i in range(j, len(word)):
                if word[i] == ".":
                    for child in cur.children:
                        if dfs(i+1, cur.children[child]):
                            return True
                    return False
                else: 
                    if word[i] not in cur.children:
                        return False
                    cur = cur.children[word[i]]
            return cur.last_char
        return dfs(0,self.root)
            
        
