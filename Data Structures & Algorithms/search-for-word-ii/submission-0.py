from typing import List
DIRS = [(1,0), (-1,0), (0, 1), (0,-1)]




class Trie:

    def __init__(self):
        self.trie = {}
    


    def insert(self, word: str) -> None:
        node = self.trie
        for ch in word:
            node = node.setdefault(ch, {})
        node["end"] = word



    def search(self, word: str) -> bool:
        node = self.trie
        for ch in word:
            if ch not in node:
                return False
            node = node[ch]
        return "end" in node



class Solution:


    def _look_around(self, board, node, i, j, taken, out) -> list:
        if "end" in node:
            out.append(node.pop("end"))

        for di, dj in DIRS:
            ni, nj = di + i, dj + j

            if not (0 <= ni < len(board) and 0 <= nj< len(board[0])):
                continue
            
            ch = board[ni][nj]


            if (ni, nj) in taken or ch not in node:
                continue
            
            taken.add((ni,nj))
            found = self._look_around(board, node[ch], ni, nj, taken, out)
            taken.discard((ni,nj))

            if not node[ch]:
                del node[ch]


        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        out = []

        for i in range(len(board)):
            for j in range(len(board[0])):
                ch = board[i][j]
                if ch in trie.trie:
                    self._look_around(board, trie.trie[ch], i, j, {(i,j)}, out)

        return out
        

        
