inputs = input().split()
A = int(inputs[0])
B = int(inputs[1])
C = int(inputs[2])

if A + B > C and A + C > B and B + C > A:
    print("fit")
else:
    print("unfit")
