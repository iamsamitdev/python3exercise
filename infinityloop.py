import time

num = 0
count = 1

while True:
    if count >= 20:
        break
    print(f"Round {count} = {num}")
    num = 0 if num == 1 else 1
    time.sleep(1)
    count = count + 1
