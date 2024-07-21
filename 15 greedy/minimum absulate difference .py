def minAbs(nums1,nums2):
    res = 0
    nums1.sort()
    nums2.sort()
    for i in range(len(nums1)):
        res += abs(nums1[i]-nums2[i])
    print(f'Minimum Absulate Value : {res}')

nums1 = [4,1,8,7]
nums2 = [2,3,6,5]    
minAbs(nums1,nums2)        