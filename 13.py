def max_number(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

one = input()
two = input()
three = input()

result = max_number(one,two,three)
print("The biggest number is", result)
