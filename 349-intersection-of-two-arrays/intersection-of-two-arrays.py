class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict_nums1, dict_nums2 = {}, {}
        res = []
        for i in nums1:
            if dict_nums1.get(i, None) == None:
                dict_nums1[i] = 1
            else:
                dict_nums1[i] += 1
        for i in nums2:
            if dict_nums2.get(i, None) == None:
                dict_nums2[i] = 1
            else:
                dict_nums2[i] += 1
                
        for i in dict_nums1:
            if i in dict_nums2:
                res.append(i)
        return res

            