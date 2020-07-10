numbers = tuple(input("Enter the number seperaed by comma: ").split(","))
print(numbers)
print("Numbers that are divisible by 5: ")
for num in numbers:
    a = int(num)
    if (a % 5 == 0):
        print(num)