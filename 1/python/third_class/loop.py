x = 1
# While Loop
while (x <= 3):
    print(x)
    x += 1

# For Loop
for i in range(10):
    print(i)

# Recursive Loop
i = 0


def Loop(ints):
    if ints == ints:
        i = ints
    elif ints >= 0:
        print(ints)
        i -= 1
    Loop(i)


Loop(5)
