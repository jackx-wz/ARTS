class Solution(object):
    def intersect(self, nums1, nums2):
        arr = []
        nums1_hash = dict()

        if len(nums1) > len(nums2):
            nums1, nums2 = (nums2, nums1)

        for x in nums1:
            nums1_hash[x] = nums1_hash.get(x, 0) + 1

        for y in nums2:
            if nums1_hash.has_key(y) and nums1_hash[y]>0:
                arr.append(y)
                nums1_hash[y] -= 1

        return arr
