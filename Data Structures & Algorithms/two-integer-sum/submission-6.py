class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Attempting the two-pass solution for this problem:
        # 1. Initialize the hashmap/dictionary:
        hashmap = {}
        
        # 2. First iterate through the entire nums array, storing the elements as keys and their indices as values:
        for index, num in enumerate(nums): 
            hashmap[num] = index

        # 3. Then iterate through the entire nums array once more, searching for the complement of the element pointed at:
        for i in range(len(nums)): 
            complement = target - nums[i]

            if complement in hashmap:
                if i != hashmap[complement]:
                    return [i, hashmap[complement]]
                else:
                    continue
            else:
                continue
        
        return ("ERROR: Complement not found.")
        
