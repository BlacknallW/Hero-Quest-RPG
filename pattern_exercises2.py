#return whether the square of array 1 is equal to array 2
array1 = [1,2,3,4]
array2 = [1,4,4,9]

def power_array(array1, array2):
    empty_list = []
    for numbers in sorted(array1):
        empty_list.append(numbers ** 2)
    if empty_list == sorted(array2):
        return True
    else:
        return False

print(power_array(array1,array2))