from array import array


def Assignment(nums):
    for num in nums:
        if nums.count(num) >= 2:
            return True
    return False


print(Assignment(array("i", [2, 14, 18, 22, 22])))
