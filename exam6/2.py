#定义一个函数 reverse_vowels(s)，参数为字符串，将其中的元音字母的顺序反转（a、e、i、o、u），返回新的字符串
def reverse_vowels(s:str):
    list1 = []
    list2 = []
    count = 0
    for num in s:
        if num == "a" or num == "e" or num == "i" or num == "o" or num == "u":
            list1.append(num)
            s=s.replace(num,"*",1)
        count += 1
    for num1 in range(0, len(list1)):
        s=s.replace("*",list1[len(list1)-1-num1],1)
    return s
print(reverse_vowels("helloew"))

