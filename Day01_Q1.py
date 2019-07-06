laps = int(input("Input the total laps:"))
output = 15
time = [4,6,8]
while (laps-3)>0:
    output += min(time)
    laps -= 1
    time[time.index(min(time))] = min(time) + 1
print(output)
     
