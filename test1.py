def big_add(num1, num2):
    # 判断小数位数，得到 n
    n1 = len(num1.partition('.')[2])  # partition 返回三元组，[2] 表示小数点右边的部分
    n2 = len(num2.partition('.')[2])
    n = max(n1, n2)

    # 同时扩大 n 倍，便于使用 Python 的整数加法
    num1 = num1.replace('.', '') + ('0' * (n - n1))  # 去掉小数点后，补 0
    num2 = num2.replace('.', '') + ('0' * (n - n2))
    print(num1, num2)

    # 使用 Python 的大数加法
    sum_final = str(int(num1) + int(num2))

    # 有小数时添加小数点
    if n > 0:
        if num1[0] == '-':
            len_num1 = len(num1) - 1
        else:
            len_num1 = len(num1)
        if num2[0] == '-':
            len_num2 = len(num2) - 1
        else:
            len_num2 = len(num2)
        if max(len_num1, len_num2) > len(sum_final):
            sum_final = '0' * (max(len_num1, len_num2) - len(sum_final)) + sum_final
        sum_final = sum_final[:-n] + '.' + sum_final[-n:]
        return sum_final

print(big_add('1', '-0.2'))