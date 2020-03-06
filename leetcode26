class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        length = 0
        for index in range(1, len(nums)):
            if nums[index] != nums[index-1]:
                length += 1
                nums[length] = nums[index]
        
        return length + 1
