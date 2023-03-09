def to_10(num):
    if num == 10:
        return 1
    if num > 10:
        return 0
    return to_10(num + 1) + to_10(num * 2)

def to_35(num):
    if num > 35 or num == 17:
        return 0
    if num == 35:
        return 1
    return to_35(num+1) + to_35(num * 2)

print(to_10(1) * to_35(10))
