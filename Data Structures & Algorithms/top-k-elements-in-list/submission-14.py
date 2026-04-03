class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency_map = {}

        for num in nums:
            if num not in frequency_map:
                frequency_map[num] = 1 
            else:
                frequency_map[num] = frequency_map[num] + 1

        sorted_frequency_map = sorted(frequency_map.items(), key=lambda x: x[1], reverse=True)

        top_k_array = []

        for index in range(k):
            top_k_array.append(sorted_frequency_map[index][0])
        
        return top_k_array

