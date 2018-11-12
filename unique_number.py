#Find the unique numbers in a given list

def uniqueNumbers(list):
    unique_numbers = []
    back_list = []

    for i in range(0,len(list)):
        if list[i] in unique_numbers:
            val = list[i]
            del unique_numbers[unique_numbers.index(val)] 
        else:
            if list[i] in back_list:
                continue
            back_list.append(list[i])
            unique_numbers.append(list[i])

    return unique_numbers

sample_list = [1,2,3,4,5,6,7,7]
sample_list_two = [44,55,66,77,44,55,66]
sample_list_three = [2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,9]

print("The unique numbers in sample_list are " + ','.join(map(str, uniqueNumbers(sample_list))))
print("The unique numbers in sample_list_two are " + ','.join(map(str, uniqueNumbers(sample_list_two))))
print("The unique numbers in sample_list_three are " + ','.join(map(str, uniqueNumbers(sample_list_three))))
