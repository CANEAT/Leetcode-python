#总体思路，排序后固定一个数，然后定义双指针滑动，重要是去重
def threeSum(nums):
    nums.sort()#paix
    res = []
    for k in range(len(nums)-1):
        if nums[k]>0:#提前终止循环
            break
        if k>0 and nums[k]==nums[k-1]:#去重
            continue
        i,j = k+1,len(nums)-1#前面的数已经用过，所以直接冲固定点开始
        while i<j:#内循环停止条件
            s = nums[k] + nums[j] + nums[i]#求和
            if s<0:#小于0需要更大的数
                i +=1
                while i<j and nums[i] == nums[i-1]:#去重
                    i +=1
            elif s>0:#大于0需要更小的数
                j-=1
                while i<j and nums[j] == nums[j+1]:#去重
                    j-=1
            else:
                res.append([nums[k],nums[i],nums[j]])#找到了
                i +=1
                j-=1
                while i<j and nums[i] == nums[i-1]:#去重
                    i +=1
                while i<j and nums[j] == nums[j+1]:#去重
                    j -=1
    return res

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))
