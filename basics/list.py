# List in Python
# List is a collection of items which are ordered and changeable. It allows duplicate members.
# List items are indexed, the first item has index [0], the second item has index [1] etc.
# List is defined by using square brackets [] and items are separated by commas.
# List can contain different data types like string, integer, float, boolean etc. It can also contain other lists (nested list).
# List is mutable, which means we can change the items in a list after it has been created. We can add, remove or modify items in a list.
# List is a built-in data type in Python and it is one of the most commonly used data structures in Python programming. It is used to store multiple items in a single variable and it provides various methods to manipulate the items in the list. Some of the common methods for lists are append(), insert(), remove(), pop(), index() etc.

plyears = ["sachin", "dhoni", "kohli", "rohit", "surya"]
print("1",plyears)#output:1 ['sachin', 'dhoni', 'kohli', 'rohit', 'surya']

# List indexing and slicing
# List indexing is used to access individual items in a list. We can use positive indexing (starting from 0) or negative indexing (starting from -1) to access items in a list.
print("2",plyears[0])#output:2 sachin
print("3",plyears[1])#output:3 dhoni
print("4",plyears[-1])#output:4 surya
print("5",plyears[0:3])#output:5 ['sachin', 'dhoni', 'kohli']
print("6",plyears[1:])#output:6 ['dhoni', 'kohli', 'rohit', 'surya']
print("7",plyears[:3])#output:7 ['sachin', 'dhoni', 'kohli']#
print("8",plyears[:])#output:8 ['sachin', 'dhoni  ', 'kohli', 'rohit', 'surya']List slicing is used to access a range of items in a list. We can specify the start index and end index to slice a list. The start index is inclusive and the end index is exclusive. If we omit the start index, it will start from the beginning of the list. If we omit the end index, it will go till the end of the list.

plyears[0] = "sachin tendulkar"#output:9 ['sachin tendulkar', 'dhoni', 'kohli', 'rohit', 'surya']# We can modify the items in a list by using indexing. We can assign a new value to an index to change the item at that index.
print("9",plyears)

plyears.append("yuvraj")#output:10 ['sachin tendulkar', 'dhoni', 'kohli', 'rohit', 'surya', 'yuvraj']# We can add items to a list by using the append() method. The append() method adds an item to the end of the list.
print("10",plyears)

plyears.insert(1, "virat")#output:11 ['sachin tendulkar', 'virat', 'dhoni', 'kohli', 'rohit', 'surya', 'yuvraj']# We can add items to a list at a specific index by using the insert() method. The insert() method takes two arguments, the first argument is the index where we want to insert the item and the second argument is the item we want to insert.
print("11",plyears)

plyears.remove("rohit")#output:12 ['sachin tendulkar', 'virat', 'dhoni', 'kohli', 'surya', 'yuvraj']# We can remove items from a list by using the remove() method. The remove() method takes one argument, the item we want to remove. It removes the first occurrence of the item in the list.
print("12",plyears)

plyears.pop()#output:13 ['sachin tendulkar', 'virat', 'dhoni', 'kohli', 'surya']# We can remove items from a list by using the pop() method. The pop() method removes the last item from the list and returns it. We can also specify an index to remove an item at a specific index.
print("13",plyears)

plyears.pop(-1)#output:14 ['sachin tendulkar', 'virat', 'dhoni', 'kohli']# We can remove items from a list by using the pop() method. The pop() method removes the last item from the list and returns it. We can also specify an index to remove an item at a specific index.
print("14",plyears)

a=plyears.index("kohli")#output:15 3# We can find the index of an item in a list by using the index() method. The index() method takes one argument, the item we want to find the index of. It returns the index of the first occurrence of the item in the list.
print("15",a)
