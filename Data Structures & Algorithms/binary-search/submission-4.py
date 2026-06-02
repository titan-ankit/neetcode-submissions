class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        
        middle_index = len(nums) // 2
        if (target>nums[middle_index]):
            result = self.search(nums[middle_index + 1:], target)
            if result == -1:
                return -1
            return middle_index+1+result
        elif (target<nums[middle_index]):
            return self.search(nums[:middle_index], target)
        else: 
            return middle_index