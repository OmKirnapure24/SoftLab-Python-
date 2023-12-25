my_list = []

n = int(input("Enter the number of elements: "))
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    my_list.append(ele)

print(f"The list is: {my_list}")
