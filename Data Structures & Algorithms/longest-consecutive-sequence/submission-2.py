class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        sorted_nums = sorted(set(nums))
        counter = 1
        res = 0
        for i,v in enumerate(sorted_nums):
            print(v)

            if i != len(sorted_nums) - 1 and sorted_nums[i+1] == v+1:
                counter+=1
            else:
                if res <= counter:
                    res = counter

                counter = 1
        return res