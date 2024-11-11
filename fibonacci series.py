#Q.4Create a while loop to print the Fibonacci series up to n terms.


n = int(input("Enter the number of terms in the Fibonacci series: "))#take user input for the number of terms in the Fibonacci series

# Initialize the first two terms of the Fibonacci series
a, b = 0, 1

# Special case: If the user asks for 1 term, just print '0'
if n == 1:
    print("Fibonacci Series:", a)
else:
    # Print the first term
    print("Fibonacci Series:", a, ",", b, end=" , ")

    # Initialize a counter for the loop
    count = 2  # We have already printed the first two terms

    
    while count < n:  # Use a while loop to generate and print the Fibonacci series

        c = a + b  # Calculate the next term
        print(c, ",", end=" ")  # Print the next term
        a, b = b, c  # Update a and b for the next iteration
        count += 1  # Increment the count

    
    print()  # Print a new line after the series
