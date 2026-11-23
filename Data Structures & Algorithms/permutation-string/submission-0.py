class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = defaultdict(int)
        freq2 = defaultdict(int)

        for i in s1:
            freq1[i] += 1
        
        l = 0
        for r in range(len(s2)):
            if r > len(s1) - 1:
                freq2[s2[l]] -= 1
                if freq2[s2[l]] == 0:
                    freq2.pop(s2[l])
                l += 1
            freq2[s2[r]] += 1

            if freq1 == freq2:
                return True


        return False
