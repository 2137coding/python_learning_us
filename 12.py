is_male = False
is_tall = True

if is_male or is_tall:
    print("you are male or tall or both")
else:
    print("you are not male or tall or both")

if is_male and is_tall:
    print("you are tall male")
elif is_male and not is_tall:
    print("short male")
elif not is_male and is_tall:
    print("tall female")
else:
    print("female!!!")
