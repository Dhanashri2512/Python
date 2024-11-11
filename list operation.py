listNums = [1,2,3,4,5,8,9] # empty list
continueYN = "yes"
choice = 0
size = 0
item = 0
i = 1
while continueYN == "yes":
    print("Press 1 to create a list of numbers dynamically...")
    print("Press 2 to display the updated list..")
    print("Press 3 to remove an element from the list...")
    print("Press 4 to insert an element at any position in the list...")
    print("Press 5 to sort a list in Ascending order...")
    print("Press 6 to sort a list in Descending order...")
    choice = int(input("Enter your choice..."))
    if (choice == 1):
        size = int(input("Enter size of the list:"))
        while i <= size:
            item = int(input("Enter number to add in the list..."))
            listNums.append(item)  # append(): adds an element at the end of the list
            print(item, " added in the list..")
            i = i + 1   
    elif (choice == 2):
        print(listNums)
    elif (choice == 3):
        item = int(input("Enter item to be removed..."))
        listNums.remove(item)  # remove(): removes an element from the list
        print(item, " is removed from the list..")
    elif (choice == 4):
        position = int(input("Enter a position to insert new item:"))
        if (position <= len(listNums)):
            item = int(input("Enter a new item to be inserted in the list..."))
            #insert(): Used to insert an element in the list at specified position.
            listNums.insert(position-1, item) 
            print(item, " inserted successfully in the list at position: ", position)
        else:
            print("Invalid position....")
    elif (choice == 5):
        listNums.sort()
        print("List is sorted, Sorted list is:\n", listNums)        
    elif (choice == 6):
        listNums.sort(reverse=True)
        print("List is sorted in reverse order, Sorted list is:\n", listNums)                
    continueYN = input("Type 'yes' to continue ..or type no")