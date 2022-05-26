from array import array


def Assignment(nums=array("i", [])):
    for num in nums:
        if nums.count(num) >= 2:
            return True
        else:
            return False


print(Assignment(array("i", [1, 2, 3, 4])))
