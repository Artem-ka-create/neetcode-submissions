class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in res:
                return [res[diff],i]
            res[n] = i


        # for i in range(0,len(nums)):
        #     for j in range(0, len(nums)):
        #         if i!=j and nums[i] + nums[j] == target:
        #             return [i,j]