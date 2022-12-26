# Create a histogram from a given list of integers.

def histrogram(nums):
    for x in nums:
        output = ''
        while x > 0:
            output = output + "x"
            x = x - 1
        print(output)

histrogram([2, 3, 6, 5])

'''
output = 
xx
xxx
xxxxxx
xxxxx
'''