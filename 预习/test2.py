file = open('TEST3.py', encoding='utf-8', mode='r+')
#print(file.readlines(5))
file.writelines(['x'])
file.close()
