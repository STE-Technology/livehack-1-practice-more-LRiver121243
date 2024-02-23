#Asks the user for the youngest and middle children ages
youngest_child = int(input(""))
middle_child = int(input(""))

#Calculates the oldest child's age
oldest_child = middle_child + middle_child - youngest_child

#outputs the oldest child's age
print(str(oldest_child))