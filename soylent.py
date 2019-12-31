n = int(input())

i = 0
while i < n:
    cal = int(input())
    if cal%400 == 0:
        print(cal//400)
    else:
        print(cal//400 + 1)
    i += 1