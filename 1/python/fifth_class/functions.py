# def Multiply(numtimesmult, *nums):
#     ans = []
#     x = 0
#     for num in nums:
#         ans.append(num)
#         ans.append(ans[x] * numtimesmult)
#         ans.pop(x)
#         x = x+1
#     for i in ans:
#         print(i)


# Multiply(2, 122, 999, 1883, 7388)

def get_number(x, y): return x+y if x > 50 else y


print(get_number(1229, 9009))
