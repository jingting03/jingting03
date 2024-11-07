number = input("")

result = []
for digit in number[::-1]:
    result.append(digit)

print(",".join(result))
