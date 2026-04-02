class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # Initialize a pointer at beginning of array and a pointer 
        # at end of array. Although the array is assumed to be 
        # 1-indexed, we still access as if 0-indexed and account 
        # for the shift later.

        head_pointer = 0
        tail_pointer = len(numbers) - 1
        
        twoSum = numbers[head_pointer] + numbers[tail_pointer]

        while twoSum != target and head_pointer != tail_pointer:
            if twoSum > target:
                tail_pointer = tail_pointer - 1
            if twoSum < target:
                head_pointer = head_pointer + 1
            twoSum = numbers[head_pointer] + numbers[tail_pointer]
        
        result = [head_pointer + 1, tail_pointer + 1]
        
        return result