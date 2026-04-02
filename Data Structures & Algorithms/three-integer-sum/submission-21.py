class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        seen_triplets = set()
        results = []

        for i in range(len(nums)):
            a = nums[i]
            seen = set()
            for j in range(i + 1, len(nums)):
                b = nums[j]
                c = -a - b
                if c in seen:
                    triplet = tuple(sorted([a, b, c]))
                    if triplet not in seen_triplets:
                        seen_triplets.add(triplet)
                        results.append(list(triplet))
                seen.add(b)

        return results