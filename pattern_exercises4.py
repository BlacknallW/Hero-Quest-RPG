#returns number of times letters appear in string
user_input = input("Type a word or phrase. ").lower()
input_histogram = {}
input_list = user_input.split(" ")

for words in input_list:
    for letters in words:
        input_histogram.update({letters : user_input.count(letters) })


print(input_histogram)