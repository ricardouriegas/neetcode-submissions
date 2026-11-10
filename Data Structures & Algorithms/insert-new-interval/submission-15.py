class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # my aproach 
        # insert the interval where its supposed to be
        intervals.append(newInterval)
        intervals.sort()

        # search and merge everything
        result = [intervals[0]]


        for i in range(1, len(intervals)):
            if result[-1][1] >= intervals[i][0]:
                result[-1][1] = max(intervals[i][1], result[-1][1])
            else:
                result.append(intervals[i])

        return result