class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency_map = {}

        for num in nums:
            if num not in frequency_map:
                frequency_map[num] = 1
            else:
                frequency_map[num] = frequency_map[num] + 1
        
        heap = []

        for num in frequency_map.keys():
            heapq.heappush(heap, (frequency_map[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []

        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result