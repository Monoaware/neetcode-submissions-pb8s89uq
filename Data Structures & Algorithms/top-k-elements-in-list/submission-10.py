class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dictionary = defaultdict(int)

        for num in nums:
            dictionary[num] = dictionary[num] + 1

        heap = []

        for key, value in dictionary.items():
            heapq.heappush(heap, (value, key))

            if len(heap) > k:
                heapq.heappop(heap)

        result = []

        while heap:
            result.append(heapq.heappop(heap)[1])
        
        return result