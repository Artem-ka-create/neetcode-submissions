class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res=[1]* len(nums)
        mult = 1
        
        for i in range(1,len(nums)):
            res[i] = nums[i-1] * mult
            mult *= nums[i-1]
        
        mult = 1

        for i in range(len(nums)-1, -1,-1):
            res[i] = res[i] * mult
            mult = mult * nums[i]
        return res