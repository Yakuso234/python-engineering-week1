from typing import List,Dict
# ======================
# 第1题：字符串反转
# ======================
def reverse_string(s:str) -> str:
    if not isinstance(s,str):
        raise TypeError("输入必须是字符串")
    return s[::-1]
# 测试第1题
print("第1题测试：", reverse_string("hello"))


# ======================
# 第2题：列表去重
# ======================

def remove_duplicates(lst:list) -> list:
    if not isinstance(lst,list):
        raise TypeError("输入必须是列表")
    a= set(lst)
    return list(a)

# 测试第2题
print("第2题测试：", remove_duplicates([1, 2, 2, 3, 3, 3]))


# ======================
# 第3题：统计词频
# ======================

def count_words(text:str) -> Dict[str,int]:
    if not isinstance(text,str):
        raise TypeError("输入必须是字符串")
    word_list = text.split()
    word_count = {}
    for i in word_list:
        if i in word_count:
            word_count[i]+=1
        else:
            word_count[i]=1
    return word_count

# 测试第3题
test_text = "I love python python python"
print("第3题测试：", count_words(test_text))


# ======================
# 第4题：斐波那契数列
# ======================
def fibonacci(n: int) -> list:
    if not isinstance(n,int):
         raise TypeError("输入必须是整数")
    if n <=0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1,1]
    else:
        fibolist = [1,1]
        for i in range(2,n):
            fibolist.append(fibolist[i-2]+fibolist[i-1])
        return fibolist

# 测试第4题
print("第4题测试：", fibonacci(10))


# ======================
# 第5题：判断回文数
# ======================
def is_palindrome(num:int) -> str:
    if not isinstance(num,int):
        raise TypeError("输入必须是整数")
    str_1 = str(num)
    str_2 = str_1[::-1]
    if str_1 == str_2:
        return "是回文数"
    else:
         return"不是回文数"
    

# 测试第5题
print("第5题测试(121)：", is_palindrome(121))
print("第5题测试(123)：", is_palindrome(123))


# ======================
# 第6题：冒泡排序（排序算法考点）
# ======================

def bubble_sort(arr:list[int]) -> list[int]:
    if not isinstance(arr,list):
        raise TypeError("输入必须是整数列表")
    arr_copy = arr.copy()
    n=len(arr_copy)
    for i in range(n-1):
        for j in range(0,n-1-i):
            if arr_copy[j]>arr_copy[j+1]:
                arr_copy[j],arr_copy[j+1]=arr_copy[j+1],arr_copy[j]
    return arr_copy


# 测试第6题
print("第6题测试：", bubble_sort([64, 34, 25, 12, 22, 11, 90]))


# ======================
# 第7题：二分查找（二分考点）
# ======================
def binary_search(arr:list[int], target:int) -> int:
    if not isinstance(arr,list) or not isinstance(target,int):
        raise TypeError("输入必须是整数列表和整数" )
    left,right = 0,len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
        
# 测试用例
test_arr = [1,2,3,4,5,6,7,8,9]
print("第7题测试(找10)：", binary_search(test_arr, 10))
print("第7题测试(找9)：", binary_search(test_arr, 9))


# ======================
# 第8题：递归实现阶乘（递归考点）
# ======================


def factorial(n:int) -> int:
    if not isinstance(n,int):
        raise TypeError("输入必须是整数")
    if n < 0:
        raise ValueError("输入必须是非负整数")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
# 测试用例
print("第八题4的阶乘：",factorial(4))


# ======================
# 第9题：两数之和（经典算法考点）
# ======================
def sum_two(nums:list[int], target: int) ->tuple:
    if not isinstance(nums,list) or not isinstance(target,int):
        raise TypeError("输入必须是整数列表和整数")
    num_dict = {}
    for index,num in enumerate(nums):
        comp_1= target - num
        if comp_1 in num_dict:
            return (num_dict[comp_1],index)
        num_dict[num] = index
    return -1
    
# 测试用例
print("第9题测试：", sum_two([2,7,11,15], 18))



# ======================
# 第10题：列表扁平化（列表进阶考点）
# ======================

def flatten_list(list_1: list) -> list:
    if not isinstance(list_1,list):
        raise TypeError("输入必须是列表")
    result= []
    for item in list_1:
        if isinstance(item,list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result
# 测试用例
print("第10题测试：", flatten_list([1, [2, [3, 4], 5], 6]))
    


