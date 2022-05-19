import array

arr = array.array("i", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

for i in arr:
    print(i)

arr.append(11)

for i in range(len(arr)):
    print(i)
