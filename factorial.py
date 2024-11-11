#Q1  WAP to get factorial of a number using while loop


num=int(input("enter the number:")) #Take a value from user
fac=1           #Initialize fac to 1,this is hold the factorial result
i = num    #Initialize i to num ;this will be used as the loop counter


while num > 1:
    fac = fac * num  
    num = num - 1


print("factorial number :",fac)    #print the factorial result
