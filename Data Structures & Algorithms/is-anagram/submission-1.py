class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = sorted(s)
        t = sorted(t)
        for char1, char2 in zip(s,t):
            if char1 == char2:
                continue
            return False
        return True

        