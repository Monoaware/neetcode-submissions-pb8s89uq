class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        maximum_length = 0

        for num in nums:
            consecutive_sequence_length = 1
            expected_num = num + 1
            while expected_num in nums:
                consecutive_sequence_length = consecutive_sequence_length + 1
                expected_num = expected_num + 1
            if consecutive_sequence_length > maximum_length:
                maximum_length = consecutive_sequence_length

        return maximum_length