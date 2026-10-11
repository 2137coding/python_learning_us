numbers = [3,5,9,4,2,8]
friends = ["Kevin", "mike","anthony", "oscar","toby"]
friends.extend(numbers) #dodaje ciąg do końca
print(friends)
friends.append("creed") #dodaje element do ciągu
print(friends)
friends.insert(1,"kelly") #dodaje element we wskazanym indeksie, przesuwając inne elementy
print(friends)
friends.remove("mike") #usuwa element
print(friends)
friends.clear() #czyści ciąg
print(friends)
friends = ["Kevin", "mike","anthony", "oscar","mike","toby"]
friends.pop() #usuwa ostatni element ciągu
print(friends)
print(friends.index("anthony")) #zwraca numer indeksu, danego elementu
print(friends.count("mike")) #liczy ile razy pojawił się dany element
numbers.sort() #porzadkuje ciąg od rosnąco lub alfabetycznie
print(numbers)
numbers.reverse() #odwraca kolejność elementów ciągu
print(numbers)
friends2 = friends.copy() #kopiuje ciąg
print(friends2)
