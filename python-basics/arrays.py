class Array:
    def __init__(self, list):
        self.list = list

    def get_min_val(self):
        min_val = self.list[0]
        for i in (self.list):
            if i < min_val:
                min_val = i

        return (min_val)

    def square_integers(self):
        square_list = []
        for i in self.list:
            square_list.append(i**2)

        return square_list

    def print_every_other_in_reverse(self):
        my_list = self.list
        reverse_list = my_list[::-2]
        return reverse_list

    def evens_only(self):
        my_list = self.list

        evens_only = []
        for i in range(len(my_list)):
            if (my_list[i]) % 2 == 0:
                evens_only.append(my_list[i])

        return evens_only

    def strings_length_2(self):
        strings_gt_than_2 = []

        for i in self.list:
            if type(i) == str:
                if len(i) >= 2:
                    strings_gt_than_2.append(i)

        return strings_gt_than_2

    def prod_of_all_others(self):
        # Use division method.
        arrayLength = len(self.list)
        sum = 0
        result = []

        for i in self.list:
            if i != arrayLength:
                sum = (i * (i + 1))

        for i in self.list:
            result.append(sum // i)

        return result


# test_List = [1, 2, 3, 4, 5, "hi"]
test_List = [1, 2, 3]
myList = Array(test_List)
# print(myList.get_min_val())
# print(myList.square_integers())
# print(myList.print_every_other_in_reverse())
# print(myList.evens_only())
# print(myList.strings_length_2())
print(myList.prod_of_all_others())
