class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        result = 0

        for i in range(len(heights)):
            tmp = i
            while stack and stack[-1][1] > heights[i]:
                index, height = stack.pop()
                result = max(result, height * (i - index))
                tmp = index
            stack.append((tmp, heights[i]))

        for i, h in stack:
            result = max(result, h * (len(heights) - i))

        return result