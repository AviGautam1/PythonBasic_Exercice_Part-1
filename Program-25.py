# Python Program to find the L.C.M. of two input number

def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm


print("The L.C.M. is", compute_lcm(15, 17))
print("The L.C.M. is", compute_lcm(222, 225))

'''
output = 
The L.C.M. is 255
The L.C.M. is 16650
'''