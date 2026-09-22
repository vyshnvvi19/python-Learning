maths=int(input("Enter the maths marks: "))
english=int(input("Enter the english marks: "))
dbms=int(input("Enter the dbms marks: "))
Average=(maths+english+dbms)/3
passed = Average>=40
print("Average: ",Average)
print("passed: ",passed)