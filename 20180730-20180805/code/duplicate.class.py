class Solution(object):
    def containsDuplicate(self, arr):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seat = {}
        for v in arr:
            if seat.has_key(v):
                return True
            else:
                seat[v] = 1

        return False