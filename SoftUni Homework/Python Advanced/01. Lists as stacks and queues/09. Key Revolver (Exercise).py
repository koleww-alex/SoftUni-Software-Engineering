from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets = list(map(int, input().split()))
key_locks = deque(list(map(int, input().split())))
mission_funds = int(input())
bullets_shot = 0
bullets_in_magazine = barrel_size
for _ in range(len(key_locks)):
    current_key_lock = key_locks[0]

    for i in range(1, len(bullets) + 1):
        current_bullet = bullets.pop()
        if current_bullet <= current_key_lock:
            key_locks.popleft()
            print('Bang!')
            bullets_in_magazine -= 1
            bullets_shot += 1
            if bullets_in_magazine == 0 and len(bullets) > 0:
                print('Reloading!')
                bullets_in_magazine += barrel_size
            break
        else:
            print('Ping!')
            bullets_in_magazine -= 1
            bullets_shot += 1
            if bullets_in_magazine == 0 and len(bullets) > 0:
                print('Reloading!')
                bullets_in_magazine += barrel_size

money_earned = mission_funds - bullets_shot * bullet_price

if len(key_locks) == 0:
    print(f'{len(bullets)} bullets left. Earned ${money_earned}')
else:
    print(f"Couldn't get through. Locks left: {len(key_locks)}")
