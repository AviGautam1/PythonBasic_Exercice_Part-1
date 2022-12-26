# Write a Python program to convert all units of time into seconds.

days = int(input("Input days: ")) * 3600 * 24
hours = int(input("Input hours: ")) * 3600
minutes = int(input("Input minutes: ")) * 60
seconds = int(input("Input seconds: "))

time = days + hours + minutes + seconds

print("The  amounts of seconds", time)


'''
Input days: 1
Input hours: 2
Input minutes: 3
Input seconds: 44
The  amounts of seconds 93824
'''