letter = input("请输入一个大写字母:")
lowercase = letter.lower()
if lowercase != "a" and lowercase != "z":
    left = chr(ord(lowercase) - 1)
    right = chr(ord(lowercase) + 1)
    print(left, right)
else:
    print(lowercase)
