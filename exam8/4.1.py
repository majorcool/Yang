# 定义一个函数，参数为一个小写英文字母组成的字符串，判断字符串是否为 '全字母短句'
# 全字母短句，是指一个句子中包含所有的英文字母（小写 a-z）
def judge(n:str):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    if n.isalpha():
        for i in n:
            if i not in alpha:
                return False
            return True
    else:
        return False

print(judge("thequickbrownfoxjumpsoverthelazydog"))