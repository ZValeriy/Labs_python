def reversestr(string1):
    strret =""
    for i in range(len(string1) - 1, -1, -1):
        strret += string1[i]
    return strret


str1 = input()
print(reversestr(str1))



