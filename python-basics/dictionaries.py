class dictionaries():
    def __init__(self):
        pass

    def most_common_element(List):
        dict = {}
        count, itm = 0, ''
        for key in reversed(List):
            dict[key] = dict.get(key, 0) + 1
            if dict[key] >= count:
                count, itm = dict[key], key
        return(itm)

    def num_of_integers(List):
        for i in List:
            if isinstance(i, int):
                print(i)


# List = ["a", 2, 3.06, "word"]
List = [2, 1, 2, 2, 1, 3] 


myDict = dictionaries
# myDict.num_of_integers(List)
print(myDict.most_common_element(List))
