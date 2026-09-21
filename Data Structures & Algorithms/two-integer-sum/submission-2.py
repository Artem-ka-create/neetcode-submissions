class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        resmap = {}
        for i,v in enumerate(nums):
            diff = target - v
            if diff in resmap:
                return [resmap[diff], i]
            resmap[v] = i


        # for i in range(0,len(nums)):
        #     for j in range(0, len(nums)):
        #         if i!=j and nums[i] + nums[j] == target:
        #             return [i,j]