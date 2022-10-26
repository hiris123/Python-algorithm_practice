input_data = input()

# Alpha랑 index로 두가지로 나눔
Alpha = input_data[0]
index = input_data[1]
index = int(index)


# 인덱스를 기준으로
# 1,8 : a,b,g,h는  수평 2 -> 수직 1 : 1개 / 나머지는 2개
# 2 ~ 7:  a,b,g,h는  수평 2 -> 수직 1 : 2개 / 나머지는 4개
# 1,2,7,8: a,h는  수직2 -> 수퍙 1 : 1개 / 나머지는 2개
# 3~5: a,h는  수직2 -> 수퍙 1 : 2개 / 나머지는 4개

n = 0
# 수평 2-> 수직 1개
if (index == 1 or index == 8):
    if (Alpha == 'a' or Alpha == "b" or Alpha == "g" or Alpha == "h"):
        n += 1
    else:
        n += 2
else:
    if (Alpha == "a" or Alpha == "b" or Alpha == "g" or Alpha == "h"):
        n += 2
    else:
        n += 4
# 수직 2 -> 수평 1개
i = 0
if (index == 1 or index == 2 or index == 7 or index == 8):

    if (Alpha == "a" or Alpha == "h"):
        i += 1
    else:
        i += 2
else:
    if (Alpha == "a" or Alpha == "h"):
        i += 2
    else:
        i += 4

print(i + n)
