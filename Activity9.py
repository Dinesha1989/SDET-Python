List1 = [13, 12, 14, 16, 17]
List2 = [19,11,18,10]

newList = []
for number in List1:
    if number % 2 != 0:
        newList.append(number)
print(newList)

for number in List2:
    if number % 2 == 0:
        newList.append(number)
print(newList)
