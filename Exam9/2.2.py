# 2.2  Capitalize the Title
# You are given a string title consisting of one or more words separated by a single space, where each word consists of English letters. Capitalize the string by changing the capitalization of each word such that:
# - If the length of the word is 1 or 2 letters, change all letters to lowercase.
# - Otherwise, change the first letter to uppercase and the remaining letters to lowercase.
# Return the capitalized title.

def title(n:str):
    title1 = n.split()
    for i in range(0, len(title1)):
        if len(title1[i]) <= 2:
            title1[i] = title1[i].upper()
        else:
            first = title1[i][:1:].upper()
            title1[i] = first + title1[i][1::].lower()
    print(title1)


title('ashj s')