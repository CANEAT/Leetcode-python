#基本思想，定义双指针，给两个列表合并排序，然后输出中间数
def findMedianSortedArrays(nums1, nums2):
    n = len(nums1)
    m = len(nums2)
    i=j=0
    if n + m == 1:
        return float((nums1+nums2)[0])
    if nums1 == []:
        if m%2 == 0:
            return (nums2[m//2]+nums2[m//2-1])/2#偶数输出中间的平均
        else:
            return float(nums2[m//2])#奇数输出中间数
    if nums2 == []:
        if n%2 == 0:
            return (nums1[n//2]+nums1[n//2-1])/2
        else:
            return float(nums1[n//2])
    count,index,count1 = 0,0,0#第一个count和index功能相同，当某个列表被指满之后第一次append最后一个数，第二次以后直接append另外一个列表
    res = []#count1的作用是控制循环的次数
    while count1<=(n+m)/2:
        count1 +=1
        if nums1[i]>=nums2[j]:
            if j == m-1:#当列表被指到最后一个
                index +=1
                if index == 1:#第一次直接append最后一个
                    res.append(nums2[j])
                if index>1:
                    res.append(nums1[i])#第二次以后就append其他列表
                    i+=1
            else:
                res.append(nums2[j])
                j +=1
        else:
            if i == n-1:
                count += 1
                if count == 1:
                    res.append(nums1[i])#同上index
                if count > 1:
                    res.append(nums2[j])
                    j +=1
            else:
                res.append(nums1[i])
                i +=1
    if (n+m)%2 == 0:
        return (res[-1]+res[-2])/2#同上偶数奇数
    else:
        return float(res[-1])

nums1 = []
nums2 = [2,4]
print(findMedianSortedArrays(nums1,nums2))


