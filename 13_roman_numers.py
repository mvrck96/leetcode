d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
s = "XVII"
a = [d[x] for x in s[::-1]]
r = a[0]
for i in range(len(a) - 1):
    if a[i + 1] >= a[i]:
        r += a[i + 1]
    else:
        r -= a[i + 1]
print(r)