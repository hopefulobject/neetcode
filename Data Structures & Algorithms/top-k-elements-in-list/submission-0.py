class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        table = {}
        intermediate = [[] for _ in range(len(nums))] 
        for num in nums:
            if table.get(num) == None:
                table[num] = 1
            else:
                table[num] += 1
        
        for num, frequency in table.items():
            print(intermediate)
            print(num, frequency)
            intermediate[frequency-1].append(num)

        i = -1
        while k != 0:
            if intermediate[i] == []:
                i -= 1
            else:
                for j in intermediate[i]:
                    output.append(j)
                k -= len(intermediate[i])
                i -= 1
            
            

            


        return output
            
        

            
            
        