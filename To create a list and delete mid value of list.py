n = int(input("Enter the number of elements: "))

elements = []
for i in range(n):
    element = input(f"Enter element {i+1}: ")
    elements.append(element)
mid = len(elements) // 2

del elements[mid]
print("The list is:", elements)
