a = set()
max_size = -1
max_min = -1
with open("26.txt") as f:
    for i in range(int(f.readline())):
        a.add(int(f.readline()))

a = sorted(list(a))

for i in range(len(a)):
    temp = 0
    last_el = a[i]
    for j in range(i+1, len(a) ):
        if last_el + 3 <= a[j]:
            temp += 1
            last_el = a[j]
    temp += 1
    if max_size <= temp:
        max_size = temp
        max_min = max(max_min, a[i])

print(max_size, max_min)
