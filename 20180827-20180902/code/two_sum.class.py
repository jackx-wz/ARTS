class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sums_dict = {}
        for k, v in enumerate(nums):
            diff = str(target-v)
            if not sums_dict.has_key(str(v)):
                sums_dict[diff] = k
            else:
                return [sums_dict[str(v)], k]
