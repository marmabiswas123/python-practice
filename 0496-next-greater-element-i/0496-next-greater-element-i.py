class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d={}
        ans=[]
        for i2 in range(len(nums2)):
            grtr=self.greater(nums2[i2:])
            d[nums2[i2]]=grtr
        for i1 in range(len(nums1)):
            ans.append(d[nums1[i1]])
        return ans
    def greater(self,arr):
        for i in arr:
            if i>arr[0]:
                return i
        return -1