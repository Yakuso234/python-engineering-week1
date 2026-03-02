# ======================
# 第1题：字符串反转
# ======================
def reverse_string(s):
    return s[::-1]
# 测试第1题
print("第1题测试：", reverse_string("hello"))


# ======================
# 第2题：列表去重
# ======================

def remove_duplicates(lst):
    a= set(lst)
    return list(a)

# 测试第2题
print("第2题测试：", remove_duplicates([1, 2, 2, 3, 3, 3]))


# ======================
# 第3题：统计词频
# ======================

def count_words(text):
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
def fibonacci(n):
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
def is_palindrome(num):
    str_1 = str(num)
    str_2 = str_1[::-1]
    if str_1 == str_2:
        return "是回文数"
    else:
         return"不是回文数"
    

# 测试第5题
print("第5题测试(121)：", is_palindrome(121))
print("第5题测试(123)：", is_palindrome(123))