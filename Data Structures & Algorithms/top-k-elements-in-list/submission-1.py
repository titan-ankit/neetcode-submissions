class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket sort fastest appraoch
        count_dict = {}
        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1
        #frequency dictionary built
        buckets = []
        for i in range(len(nums)+1):
            buckets.append([])
        #creating empty buckets

        for num, count in count_dict.items():
            buckets[count].append(num) # filling it in at index=frequency
        
        result = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result

        #gathered the top k elements backward since highest index corresponds to highest freqeunecy
        # going k indices backwards for top k frequent, as asked.