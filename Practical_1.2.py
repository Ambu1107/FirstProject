import math
n=int(input("Enter a number:"))
if(n>0 and n<9):
    print(n**2)
elif(n>10 and n<99):
    print(math.sqrt(n))
elif(n>100 and n<999):
    print(math.cbrt(n))
else:
    print("Invalid")