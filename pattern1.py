
'''
#Q1)WAP to print triangular  pattern

#printing star

for i in range(1,5):    # outer loop
    for j in range(1,i+1):  #inner loop
        print("*",end=" ")      # display star
    print()# new line after each row
    
print("-----------------------------------------")

#printing number

for i in range(1,5):   # outer loop
    for j in range(1,i+1):    #inner loop
        print(j,end=" ")             # display number
    print()  # new line after each row

print("-----------------------------------------")

#printing number 2

for i in range(1,5):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

print("------------------------------------------")

'''
'''
#Q.2)WAP TO GET FACTORIAL OF A NUMBER


num = int(input("Enter a number: "))  #Take input from user.


fact = 1  # Initialize the factorial variable

if num < 0:   # Check if the number is negative, zero, or positive
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0: 
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):  # Multiply result by each number from 1 to num
        fact *= i    # print(f"The factorial of {num} is {fact}")
    print("factorial of ", num, " is ", fact)

print("------------------------------------------------")
'''
'''
#3)WAP to traverse a list of item and find particular item is present in the list or not.

names=["neha","sahil","alex","shiv","jack"]
find="alex"
for i in names:
    if i==find:
        print("found:",find)
        break

print("------------------------------------------------")
'''
#Q4)WAP to sum first 10 natural number. 


sum = 0  # Initialize the sum to 0

for num in range(1, 11):    # Loop through numbers from 1 to 10
    sum += num   # Add the current number to the sum

print("The sum of the first 10 natural numbers is:", sum)   # Print the result
























