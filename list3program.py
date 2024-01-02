list1=[67,80,55,46,34,33,87,67,90,76,45,23,48,67,89,92]

even_count = 0
odd_count = 0


for num in list1:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1


print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)
