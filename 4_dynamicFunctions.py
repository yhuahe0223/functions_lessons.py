# def checks_3_digits(number):
#     return number in range(100,1000)

# result = checks_3_digits(68)
# print(result)

# def check_3_digits(list1):
#     for n in list1:
#         if n in range(100,1000):
#             print(True)
#         else:
#             pass
#     return False

# result = check_3_digits([555, 99, 600])
# print((result))

def check_3_digits(list1):

    three_digits_list = []
    for n in list1:
        if n in range(100,1000):
            three_digits_list.append(n)
        else:
            pass
    
    return three_digits_list

result = check_3_digits([555, 99, 600])
print((result))


# Dynamic Functions Practice #1
# Create a function (all_positives) that returns True if all the values in a list are positive, and False if at least one of the values is negative. Create a list named numbers with positive and negative values.

# Don't call the function, you just need to define it.






# Dynamic Functions Practice #2
# Create a function (sum_less) that adds the numbers of a list as long as they are greater than 0 and less than 1000, and returns the result of said sum. Create a numbers variable, storing a list of numbers so we can test it.






# Dynamic Functions Practice #3
# Create a function (count_even) that counts the number of even numbers that exist in a list (numbers), and returns the result of said count.