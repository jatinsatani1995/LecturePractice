class ReverseString:
    def __init__(self, input_string):
        self.input_string = input_string

    def reverse_words(self):
       
        words = self.input_string.split()
        reversed_words = words[::-1]
        reversed_string = ' '.join(reversed_words)

        return reversed_string


input_string = input("Enter String: ")
reverse_string_instance = ReverseString(input_string)
result = reverse_string_instance.reverse_words()

print("Original String:", input_string)
print("Reversed String:", result)
