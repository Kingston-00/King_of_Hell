num=int(input("Enter a number: "))
fact=1
cube=num**3
mul=num*num
negative=-num
while num>0:
    fact*=num
    num-=1
print("factorial is : ",fact)

print("cube:",cube)
print("mul:",mul)
print("negative:",negative)
