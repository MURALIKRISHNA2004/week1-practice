n=int(input("Enter a number: "))
odd=0
even=0
for i in range(1,11):
    p=n*i
    if p%2==0:
        print(n,"*",i,"=",p,"- Even")
        even+=1
    else:
        print(n,"*",i,"=",p,"- Odd")
        odd+=1
print("Number of Even numbers: ",even)
print("Number of Odd numbers: ",odd)            
        