class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        two_sum_dict = dict()

        for index, value in enumerate(nums):
            complement = target - value
            if complement not in two_sum_dict:
                two_sum_dict[value] = index
            else:
                if index != two_sum_dict[complement]:
                    return [two_sum_dict[complement], index]

        return