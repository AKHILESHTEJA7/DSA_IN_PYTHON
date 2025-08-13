Input = [12, 35, 1, 10, 34, 1]

largest_value = Input[0]
prev = 0
for i in range(len(Input)):
    if largest_value < Input[i]:
        prev = largest_value
        largest_value = Input[i]
    elif largest_value > Input[i] > prev:
        prev = Input[i]
    
print("second largest value is: ", prev)