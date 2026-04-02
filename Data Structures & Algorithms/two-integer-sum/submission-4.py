class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Iterate through "nums" once, adding their values to a hash map:

        hashmap = {}

        for index, num in enumerate(nums):
            hashmap[num] = index

        # Iterate through "nums" a second time, searching for its complement in the hashmap and returning the first instance found:
        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in hashmap:
                # Need to return smaller index first:
                if i != hashmap[complement]:
                    return [i, hashmap[complement]]
                else:
                    continue
                    
        return
