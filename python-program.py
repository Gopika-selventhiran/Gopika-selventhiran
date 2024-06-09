array = []
num_elements = int(input("Enter the number of elements you want to store: "))
for i in range(num_elements):
    element = input(f"Enter element {i+1}: ")
    array.append(element)
print("The elements of the array are:")
for element in array:
    print(element)
