class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}
        output = []
        for string in strs:
            arr = [0] * 26
            # setup the array for this string

            for char in string:
                arr[ord(char) - ord("a")] += 1
            

            if table.get(tuple(arr)) == None:
                table[tuple(arr)] = [string]
            else:
                table[tuple(arr)].append(string)
        
        return list(table.values())










            

        