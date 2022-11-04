#定义一个函数 perms(l)，参数为长度为 5 且只包含不重复元素的列表，返回所有的排列
def perms(l:list):
    for a in l:
        for b in l:
            for c in l:
                for d in l:
                    for e in l:
                        if a!=b and a!=c and a!=d and a!=e and b!=c and b!=d and b!=e and c!=d and c!=e and d!=e :
                            print(str(a)+str(b)+str(c)+str(d)+str(e))
perms([1,2,3,4,5])
