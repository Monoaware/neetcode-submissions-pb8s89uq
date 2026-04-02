class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hashset = set(nums)
        maximum_length = 0
        streak = 0
        expected_num = 0

        for num in nums:
            if num - 1 not in hashset:
                streak = 1
                expected_num = num + 1
                while expected_num in hashset:
                    streak = streak + 1
                    expected_num = expected_num + 1
                if maximum_length < streak:
                    maximum_length = streak
        
        return maximum_length