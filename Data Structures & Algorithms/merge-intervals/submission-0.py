class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        # print(intervals)
        result = [intervals[0]]
        
        # if theresAnInterval(intervals[0], intervals[1]):
        #     if intervals[0][-1] > intervals[1][-1]:
        #         result.append(intervals[0])
        #     else:
        #         result.append(intervals[1])
        for i in range(1, len(intervals)):
            if result[-1][1] >= intervals[i][0]:
                result[-1][1] = max(result[-1][1], intervals[i][1])
            else:
                result.append(intervals[i])
        
        return result
            