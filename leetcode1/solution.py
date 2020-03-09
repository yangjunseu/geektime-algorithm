class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = {}
        result = []
        for index in range(len(nums)):
            if nums[index] not in m:
                m[target - nums[index]] = index
            else:
                result.append(m[nums[index]])
                result.append(index)

        return result
