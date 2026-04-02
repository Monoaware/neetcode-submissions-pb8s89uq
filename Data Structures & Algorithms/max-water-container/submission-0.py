class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maximum_water = 0

        head_pointer = 0
        tail_pointer = len(heights) - 1

        while head_pointer < tail_pointer:
            container_height = min(heights[head_pointer], heights[tail_pointer])
            container_length = tail_pointer - head_pointer
            container_storage = container_height * container_length
            
            if maximum_water < container_storage:
                maximum_water = container_storage
            
            if heights[head_pointer] < heights[tail_pointer]:
                head_pointer = head_pointer + 1
            else:
                tail_pointer = tail_pointer - 1

        return maximum_water

