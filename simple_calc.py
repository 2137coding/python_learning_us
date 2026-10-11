work = True

def add(a, c):
    return int(a) + int(c)
def sub(a, c):
    return int(a) - int(c)
def mul(a, c):
    return int(a) * int(c)
def div(a, c):
    return int(a) / int(c)
def power(a, c):
    return pow(int(a), int(c))

while work == True:
    print("calculator(to exit write random number, exit, random number")
    print("number(space) char(space) number")
    a, b, c = input().split()
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


