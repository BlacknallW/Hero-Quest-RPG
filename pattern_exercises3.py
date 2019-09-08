#returns whether two input strings use the same letters the same number of times
string1 = input("Type a word here. ")
string2 = input("Now type another word to compare it to. ")

def anagram(string1, string2):
    histogram1 = {}
    histogram2 = {}
    for letters in string1:
        histogram1.update({letters : string1.count(letters)})
    print(histogram1)
    for letters in string2:
        histogram2.update({letters : string2.count(letters)})
    print(histogram2)
    if histogram1 == histogram2:
        return True
    else:
        return False
    
    
print(anagram(string1, string2))