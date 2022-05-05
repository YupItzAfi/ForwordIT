class Calculate_sum:
    def __init__(self):
        pass

    def get_value(self, number):
        i = 0
        final_list = []
        while i < number:
            i += 1
            input_val = int(input())
            input_list = [int(x) for x in str(input_val)]
            final_list.append(input_list)
        return final_list

    def calculate_sum(self, final_list):
        list_sum = []
        for x in final_list:
            sum = 0
            for y in x:
                sum += y
            list_sum.append(sum)
        return list_sum

    def print_sum(self, list_sum):
        for x in list_sum:
            print(x)


input_val = int(input())
my_obj = Calculate_sum()
final_list = my_obj.get_value(input_val)
list_sum = my_obj.calculate_sum(final_list)
my_obj.print_sum(list_sum)
