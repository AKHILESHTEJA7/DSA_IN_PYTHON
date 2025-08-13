def bubble_sort(box):
    n = len(box)
    for i in range(n):
        for j in range(0,n-i-1):
            if box[j] > box[j+1]:
                box[j], box[j + 1] = box[j + 1], box[j]
    return box

data = [5, 3, 8, 4, 2]
print("Sorted:", bubble_sort(data))