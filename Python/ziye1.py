letter = input("请输入一个大写字母:")
lower_letter = letter.lower()  # 转换成小写字母
if lower_letter != "a" and lower_letter != "z":  # 判断是否为"a"或"z"
    print(chr(ord(lower_letter) + 1))
else:
    print(lower_letter)
