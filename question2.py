customer_name=input("Enter customer name: ")
age=int(input("Enter customer age: "))
number_of_tickets=int(input("Enter number of tickets: "))
total=0
if age<12:
    ticket_price=120
    total=120*number_of_tickets
elif age>=12 and age<59:
    ticket_price=200
    total=200*number_of_tickets
else:
    ticket_price=150
    total=150*number_of_tickets
discount=0
if number_of_tickets>=5:
    discount=total*10/100

print("Customer Name: ",customer_name)
print("Age: ",age)
print("Ticket Price: Rs.",ticket_price)
print("Number of Tickets: ",number_of_tickets)
print("Total Before Discount: Rs.",total)
print("Discount: Rs.",discount)
print("Final Amount: Rs.",total-discount)
