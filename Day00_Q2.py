width = int(input("Enter the width:"))
height = int(input("Enter the height:"))
area = width * height
quad=''
if width == height:
    quad += "Sqaure"
else:
    quad += "Rectangle"
print("the area of the ",quad," is ",area)
