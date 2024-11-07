n = int(input())

passing_subjects = []  
passing_count = 0  

for _ in range(n):
    subject_info = input().split()  
    subject_name = subject_info[0] 
    score = int(subject_info[1])  

    if score >= 60: 
        passing_subjects.append(subject_name)  
        passing_count += 1  

for subject in passing_subjects:
    print(subject)

if passing_count >= ((n+1) / 2):
    print("晉級")  
else:
    print("失敗")  
