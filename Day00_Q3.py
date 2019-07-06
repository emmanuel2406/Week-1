num=list(input("input:"))
output = ''
while num != []:
    mx = max(num)
    output += str(mx)
    num.remove(mx)
print(output, "\n")
