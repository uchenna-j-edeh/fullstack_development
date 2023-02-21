# prduct of all number till n

def recurse(n):
    if  n <= 1:
        return 1
    else:
        return (recurse(n - 1) * n)

def helper(n):
    return recurse(7)

print(helper(7))