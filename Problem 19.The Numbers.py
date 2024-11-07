N, M = input().split()  

count = 0
n_length = len(N)
m_length = len(M)

for i in range(m_length - n_length + 1):
    if M[i:i + n_length] == N:
        count += 1

print(count)
