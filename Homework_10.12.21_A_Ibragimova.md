# Aliia Ibragimova
# Homework 10.12.21
# Task 1: Learn and use 3 new methods for strings. Write a code.
y = "a day consist of 24 hours, a week has 7 days, a month has 28 - 31 days, 365 - 366 days make a year"
print (y.title())
print (y.index("of"))
print (y.count ("a"))
print (y.replace("consist of", "has"))
print (y.isdigit())


# Task 2 my_list = [3, 4, 5, 6, 7, 8, 9, 10]
# a) Write a code to print sum of the first and the last elements in my_list

my_list = [3, 4, 5, 6, 7, 8, 9, 10]
y = my_list[0]
x = my_list [-1]
z = y + x
print (z)
# or just
print (my_list [0] + my_list [-1])

# b) Write a code to convert 6th element in my_list into a string and print it (without affecting the original list).
my_list = [3, 4, 5, 6, 7, 8, 9, 10]
k = str(my_list [6])
print (k)
print (type(k))

# c) Write a code to swap the third and the fourth element in my_list (without affecting the original list).

def swapList(smy_list,pos1,pos2):
    n = len(smy_list)
    # Swapping
    temp = smy_list[pos1]
    smy_list[pos1] = smy_list[pos2]
    smy_list[pos2] = temp
    return smy_list
my_list = [3, 4, 5, 6, 7, 8, 9, 10]

pos1 = 3
pos2 = 4

print(my_list)
print("Swapped list: ",swapList(my_list,pos1-1,pos2-1))


