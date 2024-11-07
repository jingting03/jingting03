inputs = input().split()
a = int(inputs[0])
b = int(inputs[1])
c = int(inputs[2])

coordinates = input().split()
X = int(coordinates[0])
Y = int(coordinates[1])

if a * X + b * Y + c == 0:
    print("YES")
else:
    print("NO")
