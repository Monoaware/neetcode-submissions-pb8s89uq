class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # Start by sorting the array to make traversal + duplicate detection easier.
        nums.sort()
        count = defaultdict(int)

        # In a dictionary, keep track of how many instances of an element there are.
        for num in nums:
            count[num] = count[num] + 1

        # Result array to be returned.
        result = list()

        # Iterate over the array and decrement the counter in the dictionary.
        for i in range(len(nums)):
            count[nums[i]] = count[nums[i]] - 1
            
            # If duplicate, skip.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Iterate over all other elements in the array 
            # and decrement the counter for the second element 
            # in the equation.
            for j in range(i + 1, len(nums)):
                count[nums[j]] = count[nums[j]] - 1

                # Check for duplicates in the second element too.
                if j - 1 > i and nums[j] == nums[j - 1]:
                    continue
                
                # Calculate the target and see if it exists within the dictionary.
                # If it does exist, and the value hasn't been "used" yet as an element 
                # in the equation, add the triplet to the answer.
                target = -(nums[i] + nums[j])
                if count[target] > 0:
                    result.append([nums[i], nums[j], target])
            
            # Reset the counter for the second element (the first element is handled by the outer loop).
            for j in range(i + 1, len(nums)):
                count[nums[j]] = count[nums[j]] + 1

        return result
        