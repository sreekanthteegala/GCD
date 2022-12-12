from math import gcd


a=int(input())
b=int(input())
y=a 
x=b
mod=1
while (mod!=0):
    mod=y%x
    gcd=x
    y=x
    x=mod
print("The gcd of",a,"and",b,"is",gcd)
    


# def gcd(a, b):
#     if(b == 0):
#         return a
#     else:
#         return gcd(b, a % b)

# a =int(input("a:"))
# b =int(input("b:"))

# print("The gcd of",a," and",b,"is : ", end="")
# print(gcd(a,b))



# def calgcd(x,y):
#     mod=1
#     while (mod!=0):
#         mod=y%x
#         gcd=x
#         y=x
#         x=mod
#     return gcd
# x=int(input("x:"))
# y=int(input("y:"))
# print(calgcd(x,y))
