import string
class WordDictionary:

    def __init__(self):
        self.trie = {}
        

    def addWord(self, word: str) -> None:
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
        
        
    def _handle_dot(self, word: str, next_dict) -> bool:


        while word and word[0] != '.':
            if word[0] not in next_dict:
                return False
            next_dict = next_dict[word[0]]
            word = word[1:]
            
            
        if not word: 
            return "end" in next_dict


        pre_word = word
        pre_dict = next_dict

        for key in pre_dict:
            if key == "end":
                continue


            next_dict = pre_dict[key]
            word = pre_word[1:]

            
            
            mismatch = False
            while word and word[0] != '.':
                if word[0] not in next_dict:
                    mismatch = True
                    break
                next_dict = next_dict[word[0]]
                word = word[1:]

            if mismatch:
                continue
            
            if not word:
                if"end" in next_dict:
                    return True
                continue


            
            if self._handle_dot(word, next_dict):
                return True
        
        return False
        


    def search(self, word: str) -> bool:
        if not self.trie:
            return False

        return self._handle_dot(word, self.trie)




                












                


 
        
