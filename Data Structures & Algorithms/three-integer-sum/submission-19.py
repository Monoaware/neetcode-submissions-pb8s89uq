class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        result = list()

        for i in range(len(nums) - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            head = i + 1
            tail = len(nums) - 1
            target = -(nums[i])

            while head < tail:
                complement = nums[head] + nums[tail]

                if complement == target:
                    result.append([nums[i], nums[head], nums[tail]])

                    while head < tail and nums[head] == nums[head + 1]:
                        head = head + 1

                    while head < tail and nums[tail] == nums[tail - 1]:
                        tail = tail - 1
                    
                    head = head + 1
                    tail = tail - 1

                elif complement < target:
                    head = head + 1

                else:
                    tail = tail - 1
        
        return result
