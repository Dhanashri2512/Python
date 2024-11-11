#wap to get area of rectangle

len = float(input("enter length of rectangle"))
wid = float(input("enter width of rectangle"))
 
def area(len,wid):
    area=len*wid
    return area
area_rect=area(len,wid)
print("area of rectangle is :",area_rect)