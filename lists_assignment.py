#1. Write a Python program to sum all the items in a list. 
    #The list should be generated using list comprehension 
    #The size of the list should be from a user input
from operator import indexOf


x=int(input("Enter the size of the list you want:"))
numbers =[x for x in range(x)]
print(numbers)#outputs the list starting from zero
sum=sum(numbers)
print(sum)#outputs the sum
#2. Write a Python program to count the number of strings 
   # where the string length is 2 or more and the first and last character
   # are same from a given list of strings. Sample List : `['abc', 'xyz', 'aba', '1221']`
lists=['abc', 'xyz', 'aba', '1221']
for element in lists:
    if len(element)>=2 and element[0]==element[-1]:
        print(element)
    else:
        continue

#3. Write a Python program to remove duplicates from a list, given list `fruits = ["Apple", "Banana", "Melon", "Banana", "Cherry", "Banana"]`
fruits = ["Apple", "Banana", "Melon", "Banana", "Cherry", "Banana"]
good_fruits =[]
for fruit in fruits:
    if fruit not in good_fruits:
        good_fruits.append(fruit)
print(good_fruits)

#4. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. Sample List : `['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']` 
colours=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
del colours[0]
del colours[3:5] 
print(colours)
#5. Write a Python program to generate and print a list except for the first 5 elements
# where the values are square of numbers between 1 and 30 (both included) 
square_numbers =[x**2 for x in range(6,31)]
print(square_numbers)