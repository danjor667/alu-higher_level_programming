#!/usr/bin/python3
for i in range(100):
    if i == 99:
        break
    print("{}{}".format(i // 10, i % 10), end=", ")
print("{}{}".format(i // 10, i % 10))
