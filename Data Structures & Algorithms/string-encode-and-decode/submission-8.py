class Solution:

    def encode(self, strs: List[str]) -> str:
        final = ""
        for string in strs:
            final += chr(len(string)) + string
        print(final)
        return final



    def decode(self, s: str) -> List[str]:
        done_for_this = 0
        final = []
        
        if s == chr(0):
            return [""]
        for i in range(len(s)-1):
            if done_for_this != 0:
                done_for_this -= 1
                continue
            number = ord(s[i])
            final.append(s[i+1:i+number+1])
            done_for_this = number
        
        return final

            
            

            

            
        
        
