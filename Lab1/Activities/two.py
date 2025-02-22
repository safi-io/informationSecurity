accumulator = 0

s=input("Enter a integer number: ")
n=int(s)

while n!=0:
    accumulator+=n
    s=input("Enter a integer number: ")
    n=int(s)

print("The sum till 0 is {}".format(accumulator))