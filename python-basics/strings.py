class String():
    def __init__(self, string):
        self.string = string

    def reverse(self):
        return self.string[::-1]

    def remove_vowels(self):
        no_vowels = []

        vowels = ["a", "e", "i", "o", "u"]
        for i in self.string:
            if i not in vowels:
                no_vowels.append(i)

        # Appends all items in no vowels into a single string
        return ''.join(no_vowels)


string_ = "facebook"
string_ = "google"

myString = String(string_)
print(myString.reverse())
print(myString.remove_vowels())
