'''
#Q.1)WAP to print triangular  pattern

*                         1                         1

* *                      1 2                      2 2 

* * *                   1 2 3                   3 3 3

* * * *                1 2 3 4                4 4 4 4

'''

#printing star

for i in range(1,5):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
    
print("-----------------------------------------")
#printing number

for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
