class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        l, r = 0, len(heights) - 1

        while l < r:
            # width = r - l
            # height = min(heights[l], heights[r])
            left_height = heights[l]
            right_height = heights[r]
            result = max(result, (r - l) * min(left_height, right_height))
            if left_height > right_height:
                r -= 1
            else:
                l += 1

        return result
            