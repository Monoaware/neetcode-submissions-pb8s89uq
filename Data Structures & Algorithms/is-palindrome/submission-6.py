class Solution:
    def isPalindrome(self, s: str) -> bool:

        concatenated_string = ""

        for char in s:
            if char.isalnum():
                concatenated_string = concatenated_string + char.lower()
        
        left_pointer = 0
        right_pointer = len(concatenated_string) - 1

        while left_pointer <= right_pointer:

            if concatenated_string[left_pointer] != concatenated_string[right_pointer]:
                return False
            
            left_pointer = left_pointer + 1
            right_pointer = right_pointer - 1
        
        return True