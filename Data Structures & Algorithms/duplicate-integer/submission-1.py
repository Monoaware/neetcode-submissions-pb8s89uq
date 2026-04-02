class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        check_duplicate = set()

        for num in nums:
            if num in check_duplicate:
                return True

            check_duplicate.add(num)

        return False

