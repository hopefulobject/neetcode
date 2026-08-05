DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


class Solution:


    def _look_around(self, board, word, i, j, taken) -> bool:
        if not word:
            return True

        for di, dj in DIRS:
            ni, nj = di + i, dj + j

            if not (0 <= ni < len(board) and 0 <= nj< len(board[0])):
                continue
            
            if (ni, nj) in taken or board[ni][nj] != word[0]:
                continue
            
            taken.add((ni,nj))
            found = self._look_around(board, word[1:], ni, nj, taken)
            taken.discard((ni,nj))

            if found:
                return True

        
        return False


        
        



    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self._look_around(board, word[1:], i, j, {(i,j)}):
                        return True
        return False

                # continue
                    


        