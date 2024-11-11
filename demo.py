list1 = [10, 20, 30, 40]
list2 = [50, 60, 70, 80]


print("list1: ", list1)
print("list2: ", list2)
for x in list2:
    list1.append(x)
print("updated list1 after appending list2 elements into it.")
print(list1)
