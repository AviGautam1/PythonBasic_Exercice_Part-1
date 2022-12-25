# Python Program to read a number n and compute n+nn+nnn.

n=int(input("Enter a number n: "))
temp=str(n)
t1=temp+temp
t2=temp+temp+temp
comp=n+int(t1)+int(t2)
print("The value is:",comp)

'''
output =
Case 1:
Enter a number n: 5
The value is: 615
 
Case 2:
Enter a number n: 20
The value is: 204060
'''