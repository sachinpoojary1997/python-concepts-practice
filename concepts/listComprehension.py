#list comprehension
# List comprehension is a concise way to create lists in Python. It allows us to create a new list by applying an expression to each item in an iterable, such as a list or a range. The syntax for list comprehension is [expression for item in iterable if condition]. The expression is evaluated for each item in the iterable, and the resulting value is added to the new list if the condition is true.

#example 1
# For example, we can use list comprehension to create a list of squares of numbers from 1 to 10:
squares = [x**2 for x in range(1, 11)]      
print("squares of numbers from 1 to 10:", squares)

#example 2
# We can also use list comprehension to create a list of even numbers from 1 to 10:
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print("even numbers from 1 to 10:", even_numbers)   

#example 3
# We can also use list comprehension to create a list of tuples, where each tuple contains a number and its square:
number_square_tuples = [(x, x**2) for x in range(1, 11)]
print("number and its square tuples:", number_square_tuples)    
      
#example 4
x = [i for i in range(5)]
print(x)

#example 5
x = [0,1,2]
y = [x.copy() for _ in range(3)]
x[0] = 99
print(y)

#example 6
x = [[1,2], 3]
y = [x.copy() for _ in range(2)]
x[0][0] = 99
print(y)

#example 7 using normal for loop
nums = [1,2,3,4]
result = []

for n in nums:
    result.append(n * 2)

print(result)

##example 7 using list comprehension for same above example7
nums = [1,2,3,4]
result = [n * 2 for n in nums]  
print(result)
