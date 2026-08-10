number_of_expenses=int(input("Enter the number of expenses: "))
expenses=[]
for i in range(number_of_expenses):
    expense=int(input("Enter the expense: "))
    expenses.append(expense)
print()
print("Total Expense:Rs.",sum(expenses))
avg=sum(expenses)/number_of_expenses
print("Average Expenses:Rs.",avg)
print("Highest Expenses:Rs.",max(expenses))
print("Lowest Expenses:Rs.",min(expenses))
count=0
for i in expenses:
    if i>500:
        count+=1
print("Number of expenses above Rs. 500: ",count)
count=0
for i in expenses:
    if i<=500:
        count+=1
print("Number of expenses less than or equal to Rs. 500: ",count)
s=0
for i in expenses:
    if i>avg:
        s+=1
print("Number of expenses above average: ",s)