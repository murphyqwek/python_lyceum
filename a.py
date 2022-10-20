from decimal import *

kv = list(map(float, "15362 19736 13864 14665 10500 8022 2262 2774 12242 18121 13882 24338".split(" ")))
price = list(map(float, "6.54 6.72 6.58 6.66 8.17 8.52 21.32 5.72 6.72 7.72 8.72 9.72".split(" ")))
cost = list(map(float, "100467.48 132625.92 91225.12 97668.9 85785 68347.44 48225.84 15867.28 39908.92 122679.17 98839.84 159170.52".split()))

original_price = float(1060811.43)
must_be_price = float(1060501.43)

def f(a, delta):
    a_ = a.copy()
    g = 0.01
    sum_ = 0
    delta_ = 0
    while delta_ <= delta:
        for i in range(12):
            a_[i] -= g
            sum_ += a_[i] * kv[i]
        delta_ = original_price - sum_
        g += 0.01
        if delta_ <= delta:
            a = a_
    return a
    
delta = original_price - must_be_price

price = f(price, delta)

for i in range(12):
    price[i] = kv[i] * price[i]
    print(kv[i], price[i], kv[i] * price[i])

print(sum(price))


