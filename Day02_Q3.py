output = ''
for i in range (122,96,-1):
    if i % 2 ==0:
        output += chr(i)
    else:
        output += chr(i).upper()
print(output)
