# Write a Python program to accept a filename from the user print the extension of that.

file_name = input("Enter The File Name You Want : " )
fn = file_name.split(".")
print("Your Extension Of File Name IS : " + fn[-1])

'''
output = 
Enter The File Name You Want : sample.py
Your Extension Of File Name IS : py
'''