# list = list(range(1, 5+1))
# print(list)
def recursion(number):
    if number == 1:
        output= number
    if number == 2:
        output = number * 1
    if number == 3:
        output = 3 * 2 * 1
    if number == 4:
        output = 4 * 3 * 2 * 1
    if number == 5:
        output = 5 * 4 * 3 * 2 * 1
    return output


print(recursion(5))
      
    

    