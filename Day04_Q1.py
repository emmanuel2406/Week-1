a = int(input("First number:"))
b = int(input("Second number:"))
ans = int(input("Answer:"))
if a+b == ans and a*b == ans:
    print("Plus or Times")
    
elif a + b == ans:
    print("Plus only")
    
elif a * b == ans:
    print("Times only")
    
else:
    print("Neither Plus nor Times")
print(a,"+",b,"=",a + b)
print(a,"*",b,"=",a*b)
