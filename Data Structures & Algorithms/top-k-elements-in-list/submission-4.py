class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        conter = {}

        for n in nums:
            conter[n] = conter.get(n,0) + 1
        sorted_nums = sorted(conter,key = conter.get, reverse = True)

        return sorted_nums[:k]

            


