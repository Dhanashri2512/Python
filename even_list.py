#WAP TO FIND EVEN NUMBERS IN THE LIST

numbers=[34,23,12,7,91,27]
even=[]  #empty list to store even numbers

for n in numbers:
    if n%2==0:
        even.append(n)
print(even)

#WAP TO ADD LIST NUMBERS.

numbers = [12,20,3,4,5]
total = 0
for number in numbers:
    total += number
print(total)

#WAP TO GET TABLE OF NUMBERS

n=int(input("enter a number:"))
for i in range(1,11):
    res=n*i
    print(res)

