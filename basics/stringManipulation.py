name = input("What's your name?: ")


def returnString(string):
    print(string)


returnString(name)
returnString(name.upper())
returnString(name.capitalize())
returnString(name.strip())  # remove spaces
returnString(name.replace('o', 'a'))

print(name[0])
print(len(name))

# Slices

name2 = "Fraschesca"
name2[0:3]
print(name2[0:3])
print(name2[:3])
print(name2[3:])
print(name2[1::2])
print(name2[::-1])
