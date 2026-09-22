class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # sorted_nums = set(nums)
        # counter = 1
        # res = 0
        # for i,v in enumerate(sorted_nums):
        #     if i != len(sorted_nums) - 1 and sorted_nums[i+1] == v+1:
        #         counter+=1
        #     else:
        #         if res <= counter:
        #             res = counter
        #         counter = 1

        num_set = set(nums)
        res = 0

        for n in nums: 
            if (n - 1) not in num_set:
                length = 0
                while ( n + length ) in num_set:
                    length+=1
                res = max(length, res)

        return res