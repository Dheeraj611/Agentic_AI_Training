class Solution:
    def maxArea(self, height):

        n = len(height)
        left = 0
        right = n - 1
        max_area = 0

        while left < right:

            h = min(height[left], height[right])
            width = right - left
            curr_area = h * width

            max_area = max(max_area, curr_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area