class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        already_existing_numbers = set() #creating a hashset
        for x in nums: 
            if x in already_existing_numbers:
                return True
            already_existing_numbers.add(x)

        return False



