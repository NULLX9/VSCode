# 从键盘输入一个大写字母,要求转换成小写字母并输出,若该小写字母不是"a"和"z"时,输出其相邻的两字母
letter = input("请输入一个大写字母:")
lower_letter = letter.lower()  # 转换成小写字母
if lower_letter != "a" and lower_letter != "z":  # 判断是否为"a"或"z"
    print(chr(ord(lower_letter) + 1))
else:
    print(lower_letter)
