class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = dict()
        i = 0
        for num in nums: 
            j = target - num
            if j in nums_dict:
                output = [nums_dict[j], i]
                return output
            nums_dict[num] = i
            i += 1

