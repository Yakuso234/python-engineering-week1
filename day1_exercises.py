from typing import List,Dict
import csv
import os
print("当前工作目录是:", os.getcwd())
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
    

# ======================
# 第11题：选择排序（排序算法考点）
# ======================
def selection_sorted(arr:list[int]) -> list[int]:
    if not isinstance(arr,list):
        raise TypeError("输入必须是整数列表")
    arr_copy = arr.copy()
    n = len(arr_copy)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if arr_copy[j] < arr_copy[min_index]:
                min_index = j
        arr_copy[i],arr_copy[min_index] = arr_copy[min_index],arr_copy[i]
    return arr_copy

# 测试用例
print("第11题测试：", selection_sorted([3,1,4,1,5,9,2,6]))  # 输出 [1,1,2,3,4,5,6,9]


# ======================
# 第12题：字典按值排序（字典进阶考点）
# ======================
def sort_dict_by_values(dict_input:dict[str,int]) -> list[tuple[str,int]]:
    if not isinstance(dict_input,dict):
        raise TypeError("输入必须是字符串键和整数值的字典")
    sorted_items = sorted(list(dict_input.items()), key=lambda x: x[1])
    return sorted_items

test_dict = {"a":5, "b":2, "c":8, "d":1}
print("第12题测试：", sort_dict_by_values(test_dict))  # 输出 [('d',1),('b',2),('a',5),('c',8)]


# ======================
# 第13题：字典合并（字典进阶考点）
# ======================
def merge_dicts(dict_1:dict,dict_2:dict) -> dict:
    if not isinstance(dict_1,dict) or not isinstance(dict_2,dict):
        raise TypeError("输入必须是字典")
    merge_dicts = dict_1.copy()
    merge_dicts.update(dict_2)
    return merge_dicts
# 测试用例
d1 = {"name":"小明", "age":20}
d2 = {"age":21, "city":"广州"}
print("第13题测试：", merge_dicts(d1, d2))  # 输出 {'name':'小明','age':21,'city':'广州'}


# ======================
# 第14题：文本文件读写（文件读写考点）
# ======================

def count_text_file(file_path:str) -> dict:
    if not isinstance(file_path,str):
        raise TypeError("文件路径必须是字符串")
    try:
        f=open(file_path,'r')
        lines_1=f.readlines()
        word_count = 0
        char_count = 0
        for line in lines_1:
            char_count += len(line)
            word_count += len(line.strip().split())
        f.close()
        return {"word_count": word_count, "char_count": char_count}
    except FileNotFoundError:
        raise FileNotFoundError("文件未找到，请检查路径是否正确")   
    except Exception as e:
        raise Exception(f"发生错误：{e}")
    
# 测试用例：
print("第14题测试：", count_text_file("test.txt"))



# ======================
# 第15题：CSV文件去重（文件读写考点）
# ======================
def simple_deduplicate(input_file:str,output_file:str):
    if not isinstance(input_file,str) or not isinstance(output_file,str):
        raise TypeError("文件路径必须为字符串")
    try:
        with open(input_file, "r",encoding="utf-8")as f:
            reader_1 = csv.reader(f)
            rows = list(reader_1)
            if not rows:
                print("文件为空")  
                return
            seen = set()
            result = list()
            for row in rows:
                row_tuple = tuple(row)
                if row_tuple not in seen:
                    seen.add(row_tuple)
                    result.append(row)
        with open(output_file,"w",encoding='utf-8',newline="")as f:
            writer = csv.writer(f)
            writer.writerows(result)
        print(f"完成，原始一共{len(rows)},现在一共{len(result)}行")
    except FileNotFoundError:
        print("找不到文件")
    except Exception as e:
        print(f"错误{e}")
# 使用
simple_deduplicate("text.csv", "simple_output.csv")
            



        
# ======================
# 第16题：回文串判断（字符串进阶考点）
# ======================
def is_palindrome_str(str_1:str) -> bool:
    if not isinstance(str_1,str):
        raise TypeError("请输入字符串")
    str_3=[str_2.lower() for str_2 in str_1 if str_2.isalnum() ]
    str_4=''.join(str_3)
    return str_4 == str_4[::-1]

# 测试用例
print("第16题测试(A man, a plan, a canal: Panama)：", is_palindrome_str("A man, a plan, a canal: Panama"))  # True
print("第16题测试(race a car)：", is_palindrome_str("race a car"))  # False


# ======================
# 第17题：最长公共前缀（字符串进阶考点）
# ======================
def longest_common_prefix(list1:list[str]) -> str:
    if not isinstance(list1,list):
        raise TypeError("请输入字符串列表")
    if len(list1) == 0:
        return ""
    same=list1[0]
    for i in list1[1:]:
        while not i.startswith(same):
            same=same[:-1]
            if len(same) == 0:
                return ""
    return same

# 测试用例
print("第17题测试([flower,flow,flight])：", longest_common_prefix(["flower","flow","flight"]))  # fl
print("第17题测试([dog,racecar,car])：", longest_common_prefix(["dog","racecar","car"]))  # 空字符串



# ======================
# 第18题：质数判断（逻辑算法考点）
# ======================
def is_prime(n:int) -> bool:
    if not isinstance(n,int):
        raise TypeError("请输入一个自然数")
    if n <= 1 :
        return False
    if n == 2:
        return True
    if n % 2 ==0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n % i ==0:
            return False
    return True

# 测试用例
print("第18题测试(17)：", is_prime(17))  # True
print("第18题测试(15)：", is_prime(15))  # False



# ======================
# 第19题：递归斐波那契第n项（递归进阶考点）
# ======================

def fibonacci_1(n: int) -> int:
    if not isinstance(n,int):
        raise TypeError("输入必须是整数")
    if n <=0:
        raise ValueError("输入必须是正整数")
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_1(n-1) + fibonacci_1(n-2)
# 测试用例
print("第19题测试：", fibonacci_1(10))  # 输出 55


# ======================
# 第20题：字典值求和（字典进阶考点）
# ======================
def sumup_dict_values(d1:dict[str,int]) -> int:
    if not isinstance(d1,dict):
        raise TypeError("输入必须是字符串键和整数值的字典")
    Toal_sum = 0
    for value in d1.values():
        if not isinstance(value,int):
            raise TypeError("字典的值必须是整数")   
        Toal_sum += value
    return Toal_sum

# 测试用例
test_d = {"a":10, "b":20, "c":30, "d":5}
print("第20题测试：", sumup_dict_values(test_d))  # 65
