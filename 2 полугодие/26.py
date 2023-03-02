a = set()
max_size = minimum = -1
with open("26.txt") as f:
    for i in range(int(f.readline())):
        k = int(f.readline())
        a.add(k)
a = sorted(list(a))
temp = 0
for i in range(len(a)):
    last_element = a[i]
    for j in range(i+1, len(a) ):
        if last_element + 3 <= a[j]:
            temp += 1
            last_element = a[j]
    temp += 1
    if max_size <= temp:
        max_size = temp
        minimum = max(minimum , a[i])
print(max_size, minimum)
