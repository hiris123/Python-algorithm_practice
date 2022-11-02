
s = input()
min_len = len(s)
# adadbdbdcdcd 가 입력으로 들어올 경우 (전체 길이 12 )
for i in range(1, min_len//2 + 1):  # 1 부터 6까지
    new_s = ''
    cnt = 1
    for j in range(0, min_len, i):  # 0 부터 12 까지 1,2,3 step을 올린다.
        if s[j:j+i] == s[j+i:j+2*i]:
            cnt += 1
        else:
            if (cnt != 1):
                new_s += str(cnt)
            new_s += s[j:j+i]
            cnt = 1
    print(new_s)
    min_len = min(min_len, len(new_s))
print(min_len)
