string=input("Enter a string: ")
upper=0
lower=0
digit=0
spaces=0
other=0
for i in string:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
    elif i.isdigit():
        digit+=1
    elif i.isspace():
        spaces+=1
    else:
        other+=1
print("Uppercase letters: ",upper)
print("Lowercase letters: ",lower)
print("Digits: ",digit)
print("Spaces: ",spaces)
print("Other characters: ",other)
