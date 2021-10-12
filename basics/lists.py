objects = ["hello", True, 1, 0, 9, False]


print(objects[2])


objects.append("z")
objects.append("zoigberg")


print(objects.pop())
print(objects)


for element in objects:
    print(element)


print(objects[::-1])
