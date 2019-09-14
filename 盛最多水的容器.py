'''
#超时，暴力遍历通过95%
def maxArea(height):
    res = 0
    n = len(height)
    for i in range(n):
        for j in range(i+1,n):
            MinHeight = min(height[i],height[j])
            area = MinHeight*(j-i)
            res = max(res,area)
    return res
'''
#定义双指针，不断去除无效的池子
def maxArea(height):
    i,j = 0,len(height)-1
    res = 0
    while i<j:
        MinHeight = min(height[i], height[j])
        area = MinHeight * (j - i)
        res = max(res,area)
        if height[j]>height[i]:
            i +=1
        else:
            j -=1
    return res
height  = [1,2,3,4,5,6,7,8]
print(maxArea(height))
