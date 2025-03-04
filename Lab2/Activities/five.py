def symetricDiffernce(a,b):
    new_set = set()
    for i in a:
        if i not in b:
            new_set.add(i)

    for i in b:
        if i not in a:
            new_set.add(i)
    
    return new_set

result = symetricDiffernce({"safi", "ahmad"}, {"safi", "ali"})
print(result)