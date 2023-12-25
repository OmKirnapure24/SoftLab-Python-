n = int(input("Enter the number of elements: "))
elements = []

for i in range(n):
    element = input(f"Enter element {i+1}: ")
    elements.append(element)

my_tuple = tuple(elements)
print("The tuple is:", my_tuple)
