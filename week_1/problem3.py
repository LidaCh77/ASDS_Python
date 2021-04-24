str1 = "How are you John?"
name = "Lida"


# 1st version

str_list = list(str1)
str_list[12:16] = "Lida"
print(str_list)
str2 = "".join(str_list)
print(str2)


# 2nd version

str2 = str1.replace("John", "Lida")
print(str2)


