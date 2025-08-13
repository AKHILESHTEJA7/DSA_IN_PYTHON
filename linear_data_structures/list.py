akhil = [12,13,1,2,3,4,5,6]

# traversal
for i in akhil:
    print(i)

# insertion
akhil.append(7)
akhil.insert(9,8)
print(akhil)

# deletion
akhil.remove(13)
akhil.pop()
print(akhil)

# search
if 5 in akhil:
    print("found")

print(akhil.index(5))

# update
akhil[5]= 90

print(akhil)