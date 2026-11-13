class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bag = defaultdict(int)
        frequency_table = [[] for i in range(len(nums) + 1)] # list where the index represent the number of repetitions and the values insisde represetnt eh numbers that have that number of repetitions given by their index

        for num in nums:
            bag[num] += 1

        for key, value in bag.items():
            frequency_table[value].append(key)
        
        result = []
        for i in range(len(frequency_table) - 1, 0, -1):
            for num in frequency_table[i]:
                if k == 0:
                    break
                result.append(num)
                k -= 1

        return result
