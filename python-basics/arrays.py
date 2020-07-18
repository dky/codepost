class Array:
    def __init__(self, list):
        self.list = list

    # Given [1, 2, 3, 4] => return 1
    # testList = [5, 2, 3, 4, 6, 1, 8]
    def get_min_val(self, list):
        # 1. Set an initial variable to self.list[0], this is the current smallest.
        current_smallest_value = self.list[0]
        # 2. Range through each item of the list comparing smallest_value with
        # next item in the list. Skipping the first.
        for i in (self.list):
            # compare the list current item being with the
            # current_smallest_value, if it's gt smallest_value return it.
            if self.list[i] < current_smallest_value:
                current_smallest_value = self.list[i]
            else:
                return current_smallest_value

    def square_integers(self, list):
        square_list = []
        for i in list:
            # print(item ** 2)
            square_list.append(i ** 2)

        return square_list

    def print_every_other_in_reverse(self, list): 
        pass

    def evens_only(self, list):
        pass

    def strings_length_2(self, list):
        pass

    def prod_of_all_others(list):
        pass


testList = [5, 2, 3, 4, 6, 1, 8]
myList = Array(testList)
print(myList.get_min_val(testList))
# print(myList.square_integers(testList))
