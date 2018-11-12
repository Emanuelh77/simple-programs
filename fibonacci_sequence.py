#FIBONACCI SEQUENCE

#return nth element in the fibonacci sequence
def fibonacci_seq(n):
    if n==0:    
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci_seq(n-1) + fibonacci_seq(n-2)

print('the 4th element in the fibonacci sequence is ' + str(fibonacci_seq(4)))
print('the 8th element in the fibonacci sequence is ' + str(fibonacci_seq(8)))
print('the 20th element in the fibonacci sequence is ' + str(fibonacci_seq(20)))


