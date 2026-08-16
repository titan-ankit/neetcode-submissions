class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = set()
        for i in range(len(nums)):
            if nums[i] in dict:
                return True
            else:
                dict.add(nums[i])

        return False