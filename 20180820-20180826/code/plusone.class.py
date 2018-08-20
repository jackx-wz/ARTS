class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        rst = ''
        new_arr = []

        for i in digits:
            rst += str(i)

        rst = int(rst) + 1

        for i in str(rst):
            new_arr.append(int(i))

        return new_arr
