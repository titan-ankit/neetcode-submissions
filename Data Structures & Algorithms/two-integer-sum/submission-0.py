class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        known_nums = {}
        for i in range(len(nums)):
            if (target - nums[i]) in known_nums:
                first_index = known_nums[target - nums[i]]
                second_index = i
                return [first_index, second_index]
            else:
                known_nums[nums[i]] = i # match key value pair in the dictionary 

