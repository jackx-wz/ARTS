class Solution(object):
    def singleNumber(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2*sum(set(arr)) - sum(arr)