
sub1 = float(input("Enter marks of DBMS: "))
sub2 = float(input("Enter marks of SQL: "))
sub3 = float(input("Enter marks of Python: "))

total = sub1 + sub2 + sub3
average = total / 3
percentage = (total / 300) * 100  

#Suraj Bhayy
print("\nTotal Marks =", total)
print("Average Marks =", average)
print("Percentage =", percentage, "%")