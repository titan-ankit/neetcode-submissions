import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency_dict = {}
        for num in nums:
            if num in frequency_dict:
                frequency_dict[num] += 1 
            else:
                frequency_dict[num] = 1

        return heapq.nlargest(k, frequency_dict.keys(), key=frequency_dict.get)