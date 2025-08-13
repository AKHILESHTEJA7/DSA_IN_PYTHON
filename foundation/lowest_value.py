i = [2 ,3, 4 ,5, 1]
lowest_value = i[0]

for j in range(0,len(i)):
    if lowest_value > i[j]:
        lowest_value = i[j]
        print("updated the lowest value.")
    
print(lowest_value," this is the lowest value i guess")