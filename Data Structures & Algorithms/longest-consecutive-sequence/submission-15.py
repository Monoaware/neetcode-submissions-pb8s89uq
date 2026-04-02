class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        # O(n log(n))
        sorted_nums = sorted(nums)

        maximum_length = 1
        streak = 0
        counter = 0
        current_num = sorted_nums[0]

        while counter < len(sorted_nums):
            if current_num == sorted_nums[counter]:
                streak = streak + 1
                while counter < len(sorted_nums) and sorted_nums[counter] == current_num:
                    counter = counter + 1
                current_num = current_num + 1   
                if maximum_length < streak:
                    maximum_length = streak
            else:
                streak = 0
                current_num = sorted_nums[counter]

        return maximum_length


