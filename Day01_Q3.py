string = input()
strng=''
for char in string:
    if ord(char)% 2 == 0:
        strng += char.upper()
    else:
        strng += char
print(strng,"\n")
