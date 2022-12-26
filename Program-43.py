# Write a Python program to filter the positive numbers from a list.

# input of list
li = []
n = int(input("Enter size of list : " ))
for i in range(0, n):
    e = int(input("Enter element of list : " ))
    li.append(e)

print("Positive numbers in", li, "are: " )

# traversing
for i in li:
    # checking condition
    if i >= 0:
        print(i, end=" ")

'''
output = 
Enter size of list : 4
Enter element of list : 2
Enter element of list : 1
Enter element of list : -2
Enter element of list : -3
Positive numbers in [2, 1, -2, -3] are: 
2 1 
'''