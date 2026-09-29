class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_numes = sorted(nums)
        res = []

        for i in range(0, len(sorted_numes)):
            target = sorted_numes[i]
            left_idx = i+1
            right_idx = len(sorted_numes)-1
            while(left_idx < right_idx):
                calc = target + sorted_numes[left_idx] + sorted_numes[right_idx]

                if calc > 0 :
                    right_idx = right_idx - 1
                elif calc < 0:
                    left_idx = left_idx + 1
                else:
                    if [target,sorted_numes[left_idx],sorted_numes[right_idx]] not in res: 
                        res.append([target,sorted_numes[left_idx],sorted_numes[right_idx]])
                    left_idx = left_idx+1
                    right_idx = right_idx-1
                    
        return res
        
        