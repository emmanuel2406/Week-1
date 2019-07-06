word = input("INPUT:")
output = ''
for char in word:
    output += ((ord(char)-96)* char)
print(output) # this program only works for alphabet characters and ignores digits
