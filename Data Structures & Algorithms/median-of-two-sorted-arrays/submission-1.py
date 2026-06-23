class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        joint = []

        for i in nums1:
            joint.append(i)

        for i in nums2:
            joint.append(i)
        
        joint.sort()

        if len(joint) % 2 == 1:
            return joint[len(joint) // 2]
        else:
            median = (joint[len(joint) // 2 - 1] + joint[len(joint) // 2]) / 2
            return median
        