print("Giraffe Academy")
print("Giraffe\n Academy") #tab
print("Giraffe\" Academy") #"
print("")
word = "Giraffe Academy"
print(word)
print(word.lower()) #funkcja wyswietli tekst małymi literami
print(word.upper()) #funkcja wyswietli tekst dużymi literami
print(word.capitalize()) #pierwsza litera duza
print(word.title()) #Zmienia pierwszą literę każdego słowa na wielką, a resztę liter w słowie na małe.
print(word.isupper()) #sprawdza czy tekst ma same duże litery, bool
print(word.upper().isupper()) #kilka funkcji po sobie
print(len(word)) #number of chars
print(word[0]) #G
print(word[8:15]) #Academy
print(word.index("G")) #0
print(word.index("f")) #4
print(word.replace("Giraffe", "Python"))
