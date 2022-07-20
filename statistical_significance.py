import random

s = 0
for x in range(2000):
    w = 0
    for y in range(86 + 80):
        w += int(random.randint(0, 1) >= 1)
    s += int(w >= 86)
print(f"p: {s/2000}")