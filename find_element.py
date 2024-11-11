#WAP TO SEARCH PARTICULAR ELEMENT IN LIST


l=[89,76,34,23,11]
searchel=34
for i in l:
    if i==searchel:
        print("element found is:",i)
        break
  else:
       print("element is not found in the list",i)
