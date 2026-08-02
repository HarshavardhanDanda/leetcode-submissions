class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        h={}
        output=[0]*len(nums1)
        for i,j in enumerate(nums1):
            h[j]=i
        print(h)
        for i in range(len(nums2)):
            print(nums2[i])
            if nums2[i] in h:
                if i == len(nums2)-1:
                    output[h[nums2[i]]]=-1
                j=i+1
                while(j<len(nums2) and nums2[i] > nums2[j]):
                    if j >= len(nums2)-1:
                        output[h[nums2[i]]]=-1
                    j+=1
                print(j)
                if j<len(nums2):
                    output[h[nums2[i]]]=nums2[j]
        print(output)     
        return output