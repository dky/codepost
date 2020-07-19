class Array:
    def __init__(self, list):
        self.list = list

    def get_min_val(self):
        list_vals = self.list
        min_val = list_vals[0]
        for i in (list_vals):
            if i < min_val:
                min_val = i

        return(min_val)

    def square_integers(self):
        square_list = []
        for i in self.list:
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


testList = [5, 2, 3, 4, 6, 8, 9, 1, 10, 20, 30]
myList = Array(testList)
print(myList.get_min_val())
print(myList.square_integers())
