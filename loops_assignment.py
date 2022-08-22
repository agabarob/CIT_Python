#1.Print First 10 natural numbers using while loop
from operator import countOf


p=1

while p<=9:
       p+=1
       print(p)

#2.Calculate the sum of all numbers from 1 to a given number.
sum = 1
counter = 1
n = int(input("Enter the value of n: "))
while counter <= n:
    sum = sum + counter
    counter = counter + 1
print("The sum is", sum)
#3. Write a program to print multiplication table of a given number. 
    # eg if number is 2, then output should be 2, 4, 6, 8 …
r=int(input("Enter the number whose multiples you want:"))
s=int(input("Enter the number of mutiples required:"))
t=r*s #determines the multiple  number s of r 
u=t+r #determine the upper boundary of the range function
for num in range(r,u,r):
    print(num)
    
#4. Write a program to display only those numbers from a list 
    # that satisfy the following conditions
    #The number must be divisible by five .
    #If the number is greater than 150, then skip it and move to the next number
    #If the number is greater than 500, then stop the loop given 
    # `numbers = [12, 75, 150, 180, 145, 525, 50]`

numbers =[12, 75, 150, 180, 145, 525, 50]
for n in numbers:
    if n%5 ==0 and n<=150:#n%5 checks the remainder.
        print(n)
    elif n>150:
        continue
    elif n>500:
        break

  
#5. Write a program to count the total number of digits in a 
    #number using a while loop. given number `4673453`
number="4673453"
n=0
for digit in number:
    n=n+1
print(n)

#6. Display numbers from -10 to -1 using while loop 
q=-11

while q<=-2:
       q+=1
       print(q)