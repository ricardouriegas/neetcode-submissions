class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1, max(piles)
        result = r
        while r >= l:
            mid = (l + r) // 2
            tmp_h = 0
            for pile in piles:
                tmp_h += math.ceil(float(pile) / mid)

            if tmp_h > h:
                l = mid + 1
            else:
                result = mid
                r = mid - 1

        return result