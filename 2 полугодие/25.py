import itertools
a = "1?2139*4"
for i in ("0123456789"):
    for j in range(4):
        zxc = list(itertools.product("0123456789", repeat=j))
        for af in zxc:
            l = a.replace('?', i).replace('*', "".join(af))
            if int(l) % 2023 == 0:
                print(l, int(l) // 2023)
