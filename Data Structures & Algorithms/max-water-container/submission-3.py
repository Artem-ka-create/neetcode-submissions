class Solution:

    def maxArea(self, heights: List[int]) -> int:
        res = 0
        left_idx = 0
        right_idx = len(heights)-1
        while(left_idx<right_idx):
            area = (right_idx - left_idx) * (min(heights[left_idx],heights[right_idx]))
            if area > res:
                res = area
            
            if heights[left_idx] <= heights[right_idx]:
                left_idx = left_idx + 1
            else:
                right_idx = right_idx - 1
            

        return res



