class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # Not working
        # intervals = sorted(firstList + secondList)
        # print(intervals)
        # result = []

        # for i in range(1, len(intervals)):
        #     if intervals[i][0] <= intervals[i-1][1]:
        #         if intervals[i][1] >= intervals[i-1][0]:
        #             result.append([intervals[i][0], intervals[i-1][1]])
        #         elif intervals[i][1] < intervals[i-1][0]:
        #             result.append([intervals[i][0], intervals[i][1]])

        # return result


        # two pointer solution
        result = []
        i = j = 0


        while i < len(firstList) and j < len(secondList):
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])

            if start <= end: # see if theres an overlap
                result.append([start, end])
            # if there no overlap then dont have to do something about it

            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return result




