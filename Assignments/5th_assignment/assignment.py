def Assignment_Intercession():
    num1 = [1001, 981]
    num2 = [9, 8, 7, 4, 1, 4, 1001, 981, 9, 65]

    m = []

    if num1.__len__() > num2.__len__():
        greater_list = num1
        smaller_list = num2
    else:
        greater_list = num2
        smaller_list = num1

    for i in smaller_list:
        for j in greater_list:
            if i == j:
                m.append(i)
            if
            m.append(j)
            return m


print(Assignment_Intercession())
