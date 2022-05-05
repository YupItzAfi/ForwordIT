def Input(ops=[]):
    numofel = int(input("Enter number of elements: "))
    if numofel == 0 or None:
        return ops
    lis = []
    for i in range(0, numofel):
        input_ = input(f"Enter Value No. {i+1}")
        lis.append(input_)
    return lis


def Game_Scores_Calculator(ops=[]):
    record = []
    for chars in ops:
        if str(chars).lstrip('-').isnumeric():
            record.append(int(chars))
        if chars == "C":
            print(f"Invalidating Number: {record[-1]}")
            record.pop(record[-1])
        if chars == "D":
            print(
                f"Multiplying Number to List: {record[-1]} * 2")
            record.append(record[-1]*2)
        if chars == "+":
            print(f"Adding Numbers: {record[-1]} + {record[-2]}")
            record.append(record[-1] + record[-2])
    return f"Answer: {sum(record)}"


print(Game_Scores_Calculator(Input()))
