myList1 = []
print("Enter Objects of first list...")

for i in range(5):
    val = int(input("Enter a value:"))
    myList1.append(val)

myList2 = []
print("Enter Objects of secpond list...")

for i in range(5):
    val = int(input("Enter a value:"))
    myList2.append(val)

myList3 = myList1 + myList2
print(myList3)