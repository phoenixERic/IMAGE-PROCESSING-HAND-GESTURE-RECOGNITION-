temp1=float(input("enter the temp1"))
temp2=float(input("enter the temp2"))
weight=float(input("enter the weight of water "))

energy=abs(weight*(temp2-temp1)*4184)
print(energy)  