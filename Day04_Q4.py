word = input()
output = ''
for char in word:
    if char.isupper() is True:
        output += char.lower()
    elif char.islower() is True:
        output += char.upper()
    else:
        output += char
print(output)
