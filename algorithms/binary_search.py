def binarysearch(paper,target):
    low = 0
    high = len(paper) - 1

    while low <= high:
        mid = (low + high)//2

        if paper[mid] == target:
            return mid
        elif paper[mid] <  target:
            low  = mid + 1
        else:
            high = mid - 1
    return -1

paper = [1, 3, 5, 7, 9, 11, 13]
target = 7
result = binarysearch(paper,target)

print(result)