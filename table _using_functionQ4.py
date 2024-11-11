#Q.4)WAP to get table of a number using function

num=int(input("enter a number"))

def table(num):
    for i in range(1,11):
        ans=i*num
        print(ans)
table(num)
