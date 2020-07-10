numbers = list(input("Enter the comma seperated numbers: ").split(","))
print(numbers)

first_element = numbers[0]
last_element = numbers[-1]

if first_element == last_element:
    print ("True")
else:
    print("False")
    
