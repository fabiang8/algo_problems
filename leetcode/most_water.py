class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1 # last position in height array
        max_area = 0

        while(left < right): # while left is not right , return the max between max_area and the new area
            max_area = max(max_area, min(height[left],height[right])*(right-left)) 
            print(right,left)
            print(max_area)
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1

        return max_area
