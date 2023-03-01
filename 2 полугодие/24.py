a = []
with open("24.txt") as f:
    a = [x for x in f.readline()]
res = 0
temp = 0
for i in range(0, len(a) - (len(a) & 1), 2):
    if a[i] + a[i + 1] in ("DA", "FA", "CA", "DO", "FO", "CO"):
        temp += 1
    else:
        res = max(res, temp)
        temp = 0
print(res)
