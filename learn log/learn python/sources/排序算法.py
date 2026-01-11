#基于比较的排序算法至少需要O（n log n）的时间复杂度
#冒泡排序算法
def buble_sort(lst):
    l = len(lst)
    for i in range(l):
        for j in range(l-i-1):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
    return lst
#最坏情况 O（n^2）

#归并排序算法
def merge_sort(lst):
    l = len(lst)
    if l <= 1:
        return lst
    mid = l//2
    first,last = lst[:mid],lst[mid:]
    first = merge_sort(first)
    last = merge_sort(last)
    list = []
    i,j = 0,0
    while i < mid and j < l-mid:
        if first[i] > last[j]:
            list.append(last[j])
            j += 1
        else:
            list.append(first[i])
            i += 1
    list.extend(first[i:])
    list.extend(last[j:])
    return list
#O（n log n）
#递归方程 ： T(n) = 2 T(n/2) + O(n)

lst = [3,2,56,47,23,45]
result = merge_sort(lst)
print(result)

#快速排序


#不同于比较 这里的排序方法只需要线性的时间复杂度

'''nums = [17,23,47,22,19]
#基数排序+计数排序
def count_sort(nums,exp):

    count = [0]*10

    for num in nums:
        index = (num//exp)%10
        count[index] += 1

    output = [0]*len(nums)
    for i in range(len(nums)):
        index = (nums[i]//exp)%10
        output[count[index]] = nums[i]


def linear_sort(nums):

    #取nums的长度为基数，ps：最大数字是n的多少指数幂则位数为多少

    #计算对应的键
    max_num = max(nums)
    exp = 1
    while max_num // exp > 0:
        count_sort(nums,exp)
        exp *= 10

    return nums 
'''
nums = [17,23,47,22,19]
#以10为基数结合计数排序的线性时间复杂度的排序
def count_sort(nums,exp):
    count = [0]*10
    output = [0]*len(nums)

    for num in nums:
        count[(num//exp)%10] += 1
    
    for i in range(1,10):
        count[i] += count[i-1]

    #先放进去的先拿出来 保证最后顺序是对的
    i = len(nums)-1
    while i >= 0:
        index = (nums[i]//exp)%10
        output[count[index]-1] = nums[i]
        count[index] -= 1
        i -= 1
    
    for i in range(len(nums)):
        nums[i] = output[i]

        
def linear_sort(arr):
    exp = 1
    while max(arr)//exp > 0:
        count_sort(arr,exp)
        exp *= 10
    return arr
