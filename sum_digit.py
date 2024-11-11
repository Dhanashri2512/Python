#Q.3)Write a while loop to calculate the sum of digits of a given number.



num = int(input("Enter a number: ")) #take input from user

sum = 0  # Initialize sum variable to 0

while num != 0:  # Continue loop until num becomes 0

    
    last_digit = num % 10   # Extract last digit using modulus operator (%)
    
    sum+= last_digit   # Add last digit to sum
   
    num = num // 10    # Remove last digit by performing integer division by 10

print("Sum of digits:", sum)  # Print sum of digits

