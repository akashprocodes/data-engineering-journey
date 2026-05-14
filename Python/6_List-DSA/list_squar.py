
# Print squar
#-----------
list = [1, 2, 3, 4, 5] # Original list

squared_list = [] # Empty list

for i in list: 
    squared_list.append(i * i) # adding to new list

print(squared_list) 


#One more option with the help of list comprehension
#---------------------------------------------------
list = [1, 2, 3, 4, 5, 6] # Original list  

squared_list = [i * i for i in list] # List comprehension to square elements
print(squared_list)


# Insert Items The insert() method inserts an item at the specified index:
#-------------------------------------------------------------------------
My_list = ["apple", "banana", "cherry"]
My_list.insert(2, "watermelon") 
print(My_list)