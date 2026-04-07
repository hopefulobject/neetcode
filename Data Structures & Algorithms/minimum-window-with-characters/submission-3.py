import string
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        remaining = {}
        overall = len(t)
        minimum = ""
        minimum_length = len(s)+1

        for l in t:
            if l not in remaining:
                remaining[l] = 0
            remaining[l] += 1

        l = None

        for r in range(len(s)):

            if s[r] not in remaining:
                continue

            if l == None:
                l = r
            
            if remaining[s[r]] > 0:
                overall -= 1
            remaining[s[r]] -= 1


            while True:
                if s[l] not in remaining:
                    l+=1
                    continue
                
                if remaining[s[l]] < 0:
                    remaining[s[l]] += 1
                    l+=1
                    continue
                break

            if overall == 0 and r-l < minimum_length:
                minimum = s[l:r+1]
                minimum_length = r-l
            
        return minimum
                 




        


        