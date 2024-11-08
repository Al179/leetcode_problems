class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length_of_nums = len(nums)
        for i in range(length_of_nums):
            for j in range(i+1,length_of_nums):
                if(nums[i]+nums[j]==target):
                    return [i, j]
             
            