akhil = "hello to the akhil world(hell)"

# traversal
for i in akhil:
    print(i)

# search
if "to" in akhil:
    print("found it")

print(akhil.find("to"))

# update
vishnu = list(akhil)
vishnu[0],vishnu[13],vishnu[19] = "H","A","W"
akhil = "".join(vishnu)
print(akhil)

# slicing
found = akhil[::-1]
print(found)
found1 = akhil[13:18]
print(found1)

# others
ind = akhil.split()
print(ind)