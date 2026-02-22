# Looping through a list
# We can loop through a list by using a for loop. The for loop iterates through each item in the list and executes the block of code for each item. We can also use a while loop to loop through a list, but it is less common than using a for loop. In a for loop, we can access the index of the current item by using the enumerate() function. The enumerate() function returns both the index and the value of each item in the list.
players = ["virat", "dhoni", "kohli", "rohit", "surya"]
for player in players:
    print("player:", player)

#methode 1
# We can also use a for loop to access the index of each item in the list by using the range() function. The range() function returns a sequence of numbers, which we can use to access the index of each item in the list.
for i in range(len(players)):
    print("index:", i, "player:", players[i])

#methode 2
# We can also use a for loop to access the index of each item in the list by using the enumerate() function. The enumerate() function returns both the index and the value of each item in the list.
for index, player in enumerate(players):
    print("index:", index, "player:", player)
  
#above both the enumerate() function and the range() function can be used to loop through a list and access both the index and the value of each item in the list. The enumerate() function is more concise and easier to read than using the range() function, so it is generally recommended to use the enumerate() function when looping through a list.

#len() function is used to get the length of a list. It returns the number of items in the list. We can use the len() function to get the length of a list and use it in a for loop to loop through the list.
lenght=len(players) 
print("length of players list:", lenght)

# sorted_players = sorted(players) #sorted() function is used to sort a list in ascending order. It returns a new list that is sorted in ascending order. We can also use the sort() method to sort a list in place, which means it modifies the original list and does not return a new list.
# print("sorted players list:", sorted_players)

players.sort() #sort() method is used to sort a list in place, which means it modifies the original list and does not return a new list. It sorts the list in ascending order by default, but we can also specify the sorting order by using the reverse parameter.
print("players list after sorting:", players)   

players.sort(reverse=True) #sort() method is used to sort a list in place, which means it modifies the original list and does not return a new list. It sorts the list in ascending order by default, but we can also specify the sorting order by using the reverse parameter.
print("players list after sorting in reverse order:", players)
