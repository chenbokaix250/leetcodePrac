# python字符串操作常用方法

## 1. 字符串连接

### 字符串连接
```
def string_concat_example():
       s1 = "Hello"
       s2 = "World"
       # 方法1：使用+运算符
       result1 = s1 + " " + s2  # "Hello World"
       
       # 方法2：使用join方法
       result2 = " ".join([s1, s2])  # "Hello World"
       
       # 方法3：使用格式化字符串
       result3 = f"{s1} {s2}"  # "Hello World"
       
       # 方法4：使用字符串格式化
       result4 = "%s %s" % (s1, s2)  # "Hello World"
       result5 = "{} {}".format(s1, s2)  # "Hello World"
       
       return result1, result2, result3, result4, result5
```

### 字符串切片

```
def string_slicing_example():
       s = "Hello World"
       
       # 基本切片 [start:end:step]
       first_five = s[:5]  # "Hello"
       last_five = s[-5:]  # "World"
       middle = s[2:8]  # "llo Wo"
       
       # 反转字符串
       reversed_str = s[::-1]  # "dlroW olleH"
       
       # 每隔一个字符
       every_other = s[::2]  # "HloWrd"
       
       return first_five, last_five, middle, reversed_str, every_other
```

### 字符串常用方法

```
   def common_string_methods_example():
       s = "  Hello, World!  "
       
       # 大小写转换
       upper_case = s.upper()  # "  HELLO, WORLD!  "
       lower_case = s.lower()  # "  hello, world!  "
       title_case = s.title()  # "  Hello, World!  "
       capitalize = s.capitalize()  # "  hello, world!  "
       swapped_case = s.swapcase()  # "  hELLO, wORLD!  "
       
       # 空格处理
       stripped = s.strip()  # "Hello, World!"
       left_stripped = s.lstrip()  # "Hello, World!  "
       right_stripped = s.rstrip()  # "  Hello, World!"
       
       # 查找与替换
       found_index = s.find("World")  # 8
       found_index_with_start = s.find("o", 5)  # 8 (从索引5开始查找)
       replaced = s.replace("World", "Python")  # "  Hello, Python!  "
       
       # 分割与拼接
       split_result = "apple,banana,orange".split(",")  # ["apple", "banana", "orange"]
       joined_result = "-".join(["apple", "banana", "orange"])  # "apple-banana-orange"
       
       # 检查方法
       starts_with = "Hello".startswith("He")  # True
       ends_with = "Hello".endswith("lo")  # True
       is_digit = "12345".isdigit()  # True
       is_alpha = "Hello".isalpha()  # True
       is_alphanumeric = "Hello123".isalnum()  # True
       is_lower = "hello".islower()  # True
       is_upper = "HELLO".isupper()  # True
       
       return upper_case, lower_case, stripped, found_index, replaced, split_result, joined_result
```


# 2. 高级字符串操作


### 使用正则表达式
```
   import re
   
   def regex_operations_example():
       text = "The date is 2023-04-15 and time is 14:30:25"
       
       # 匹配日期
       date_pattern = r"\d{4}-\d{2}-\d{2}"
       dates = re.findall(date_pattern, text)  # ["2023-04-15"]
       
       # 匹配时间
       time_pattern = r"\d{2}:\d{2}:\d{2}"
       times = re.findall(time_pattern, text)  # ["14:30:25"]
       
       # 替换文本
       modified_text = re.sub(r"\d+", "X", text)  # "The date is X-X-X and time is X:X:X"
       
       # 拆分文本
       words = re.split(r"\s+", text)  # ["The", "date", "is", "2023-04-15", "and", "time", "is", "14:30:25"]
       
       # 检查匹配
       has_date = bool(re.search(date_pattern, text))  # True
       
       return dates, times, modified_text, words, has_date
```

### 使用字符串格式化

```
def string_formatting_example():
       name = "Alice"
       age = 30
       height = 1.75
       
       # 基本格式化
       basic = f"{name} is {age} years old"  # "Alice is 30 years old"
       
       # 数字格式化
       float_format = f"Height: {height:.2f}m"  # "Height: 1.75m"
       percentage = f"Complete: {0.7523:.1%}"  # "Complete: 75.2%"
       padding = f"ID: {42:05d}"  # "ID: 00042"
       
       # 对齐
       left_aligned = f"{name:<10}|"  # "Alice     |"
       right_aligned = f"{name:>10}|"  # "     Alice|"
       center_aligned = f"{name:^10}|"  # "  Alice   |"
       
       return basic, float_format, percentage, padding, left_aligned, right_aligned, center_aligned

```


# 3. Leetcon常用字符串技巧

### 判断回文字符串

```
def is_palindrome(s):
       # 移除非字母数字字符并转为小写
       s = ''.join(c.lower() for c in s if c.isalnum())
       # 判断正序和逆序是否相同
       return s == s[::-1]
```


### 字符技术

```
from collections import Counter
   
   def character_frequency(s):
       # 方法1：使用Counter
       freq_counter = Counter(s)
       
       # 方法2：使用字典
       freq_dict = {}
       for char in s:
           freq_dict[char] = freq_dict.get(char, 0) + 1
       
       # 方法3：获取最常见的字符
       most_common = freq_counter.most_common(1)[0]  # (字符, 出现次数)
       
       return freq_counter, freq_dict, most_common
```

### 整数转罗马数字
```
   def integer_to_roman(num):
       values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
       symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
       
       result = []
       for i in range(len(values)):
           while num >= values[i]:
               num -= values[i]
               result.append(symbols[i])
       
       return ''.join(result)
```
   
### 罗马数字转整数

```
   def roman_to_integer(s):
       values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
       result = 0
       
       for i in range(len(s)):
           if i > 0 and values[s[i]] > values[s[i-1]]:
               result += values[s[i]] - 2 * values[s[i-1]]
           else:
               result += values[s[i]]
       
       return result
```



