class Solution:
    def reverseBits(self, n: int) -> int:
        output = 0
        for i in range(32):
            mask = 1 << i
            if mask & n:
                output = output ^ (1 << 31 - i)

        return output