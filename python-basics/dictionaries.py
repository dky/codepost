class dictionaries():
    def __init__(self):
        pass

    def most_common_element(List):
        dict = {}
        count, itm = 0, ''
        for key in List:
            dict[key] = dict.get(key, 0) + 1
            if dict[key] >= count:
                count, itm = dict[key], key
        return(itm)

    def find_elements_by_occurance(List, occurs):
        dict = {}
        most_occurring_element = 0

        # O(n)
        for key in (List):
            if key in dict:
                dict[key] += 1
            else:
                dict[key] = 1

        # O(n)
        for k, v in dict.items():
            if v == occurs:
                most_occurring_element = k

        return most_occurring_element

    def num_of_integers(List):
        for i in List:
            if isinstance(i, int):
                return(i)


# List = ["a", 2, 3.06, "word"]
# List = [2, 1, 2, 2, 1, 3]
List = [1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 5]


myDict = dictionaries
# myDict.num_of_integers(List)
# print(myDict.most_common_element(List))
print(myDict.find_elements_by_occurance(List, 3))
