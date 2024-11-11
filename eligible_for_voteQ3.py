#Q.3)WAP to check whether person can vote or not using function.

age=int(input("Enter your age:"))

def vote(age):
    if age >= 18:
        print("you are eligible to vote ")
    else:
        print("you are not eligible to vote ")
vote(age)
