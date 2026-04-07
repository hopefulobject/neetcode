class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for char in s:
            if count.get(char) == None:
                count[char] = 1
            else:
                count[char] +=1
        for char in t:
            if count.get(char) == None or count.get(char) == 0:
                return False 
            count[char] -= 1
        return True


        