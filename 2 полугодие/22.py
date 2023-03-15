ans = []
with open("22.txt") as f:
    for line in f.readlines():
        process, time, ref = line.split()
        process = int(process)
        time = int(time)
        ref = list(map(int, ref.split(';')))
        if ref[0] == 0:
            ans.append(time)
            continue
        if len(ref) == 1:
            ans.append(ans[ref[0] - 1] + time)
            continue
        ans.append(max(ans[ref[0] - 1], ans[ref[1] - 1]) + time)

print(max(ans))
