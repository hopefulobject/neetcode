class PrefixTree:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        if word[0] in self.trie: 
            next_dict = self.trie[word[0]]
            word = word[1:]

            while word:

                if word and word[0] in next_dict:
                    next_dict = next_dict[word[0]]
                    word = word[1:]

                else:
                    next_dict[word[0]] = {}
                    next_dict = next_dict[word[0]]
                    word = word[1:]
            next_dict["end"] = True
            
        else:
            self.trie[word[0]] = {}
            next_dict = self.trie[word[0]]
            word = word[1:]
            while word:
                next_dict[word[0]] = {}
                next_dict = next_dict[word[0]]
                word = word[1:]
            
            next_dict["end"] = True



    def search(self, word: str) -> bool:
        if word[0] in self.trie:
            next_dict = self.trie[word[0]]
            word = word[1:]
            
            while word:
                if word and word[0] in next_dict:
                    next_dict = next_dict[word[0]]
                    word = word[1:]
                else:
                    return False
            if "end" in next_dict:
                return True

        return False

        

    def startsWith(self, prefix: str) -> bool:
        if prefix[0] in self.trie:
            next_dict = self.trie[prefix[0]]
            prefix = prefix[1:]
            
            while prefix:
                if prefix and prefix[0] in next_dict:
                    next_dict = next_dict[prefix[0]]
                    prefix = prefix[1:]
                else:
                    return False
        else:
            return False

        return True
        
        
