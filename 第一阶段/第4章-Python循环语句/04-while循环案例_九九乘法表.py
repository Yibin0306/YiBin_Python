i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j}*{i}={j*i}\t" , end='')
        j += 1
    i = i + 1
    print()# 换行