n = int(input("Enter the number of elements: "))

elements = []

for i in range(n):
    element = input(f"Enter element {i+1}: ")
    elements.append(element)

elements.sort()

print("The sorted list is:", elements)

elements.reverse()

print("The reversed list is:", elements)
