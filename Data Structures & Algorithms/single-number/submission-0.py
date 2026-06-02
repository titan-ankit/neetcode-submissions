class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        output = 0
        for x in nums: 
            output ^= x
        return output