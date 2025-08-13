def reverse(value):
    if len(value) <= 1:
        return value
    else:
         return reverse(value[1:])+ value[0]

print(reverse("string"))