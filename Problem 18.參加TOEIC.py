n = int(input(""))

scores = []
highest_score = 0
above_900_count = 0
between_600_700_count = 0
total_score = 0

for _ in range(n):
    score = int(input(""))
    scores.append(score)
    highest_score = max(highest_score, score)
    total_score += score

    if score >= 900:
        above_900_count += 1
    if 600 <= score <= 700:
        between_600_700_count += 1

average_score = round(total_score / n, 1)

print(f"{highest_score}")
print(f"{above_900_count}")
print(f"{between_600_700_count}")
print(f"{average_score}")
