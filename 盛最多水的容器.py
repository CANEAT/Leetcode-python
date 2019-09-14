'''
#超时
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