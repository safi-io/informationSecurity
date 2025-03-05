# Getting Input and Storing in LIST
# countries = []
#
# for i in range(1, 4):
#     country = input(f"Enter your {i} favourite country: ")
#     countries.append(country)
#
# print(type(countries))

def is_palindrome():
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True

list1 = [1,2,1]
list2 = list1.copy()
list2.reverse()

print(is_palindrome())