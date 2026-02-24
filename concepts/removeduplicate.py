##method 1
# # We can remove duplicates from a list by using the set() function. The set() function
# # takes a list as an argument and returns a set, which is an unordered collection of unique items. We can then convert the set back to a list to get a list of unique items.
# number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # Remove duplicates from a list
# number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
# unique_number = list(set(number))
# print("unique number list:", unique_number)

##method 2
#without using set() function
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
res= []
for num in number :
    if num not in res:
        res.append(num)
print("unique number list:", res)