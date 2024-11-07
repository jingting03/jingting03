distance = int(input())

distance_cm = distance * 100

my_speed_cm_per_sec = 100
friend_speed_cm_per_sec = 30 * 2.54  

time_seconds = distance_cm / (my_speed_cm_per_sec - friend_speed_cm_per_sec)

print(int(time_seconds) + 1)
