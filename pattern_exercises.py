#return whether two arrays have the same frequency of characters
array1 = [8,0,4,4]
array2 = [8,4,0,4]

def frequency_calculator(array1, array2):
    if sorted(array1) == sorted(array2):
        return True
    else:
        return False