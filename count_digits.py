#Q.2)Write a while loop that counts the number of digits in a given number


num = int(input("Enter a number: "))   # Tke input from the user

count = 0     # Initialize count variable to 0

while num != 0:      # Continue loop until num becomes 0
    num = num // 10   # Remove last digit by performing integer division by 10
    count += 1       # Increment count for each digit
Enter a number: 12345678
Number of digits: 8

print("Number of digits:", count)   # Print total count of digits



