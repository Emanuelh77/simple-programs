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

    print(unique_numbers)