class Solution(object):
    def reverseArray(self, nums, start, end):
        while start < end:
            nums[start],nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return
        
        n = len(nums)
        k = k % n

        self.reverseArray(nums, n-k, n-1)
        self.reverseArray(nums, 0, n-k-1)
        self.reverseArray(nums, 0, n-1)
