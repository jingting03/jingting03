X,Y=input().split()
x=int(X)
y=int(Y)

r=100
d=(x**2 + y**2)**0.5

if (d<=r):
    print("inside")

else:
    print("outside")
