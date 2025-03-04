def isPalindrome(word):
    temp = word[::-1] # slicing method(start, stop, step)
    if word.capitalize() == temp.capitalize():
        return True
    else:
        return False


print(isPalindrome("121"))