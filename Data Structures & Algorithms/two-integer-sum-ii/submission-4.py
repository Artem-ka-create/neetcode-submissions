class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        pointer1 = 0
        pointer2 = len(numbers)-1
        for i in range(0,len(numbers)):
            if target < numbers[pointer1] + numbers[pointer2]:
                pointer2 -=1
            elif target > numbers[pointer1] + numbers[pointer2]:
                pointer1 +=1
            else:
                break

        return [pointer1+1, pointer2+1]
