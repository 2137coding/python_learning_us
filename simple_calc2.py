work = True

def add(a, c):
    return (a) + (c)
def sub(a, c):
    return (a) - (c)
def mul(a, c):
    return (a) * (c)
def div(a, c):
    return (a) / (c)
def power(a, c):
    return pow((a), (c))

while work == True:
    print("calculator(to exit write exit as operator")
    a = float(input())
    b = input()
    c = float(input())
    if b == "+":
        print(add(a, c))
    elif b == "-":
        print(sub(a, c))
    elif b == "*":
        print(mul(a, c))
    elif b == "/":
        print(div(a, c))
    elif b == "^":
        print(power(a, c))
    elif b == "exit":
        break
    else:
        print("Error: undefined operation")

