from datetime import timedelta
from time import sleep

import redis

# В Redis можно устанавливать срок действия ключа.

r = redis.Redis()
# Вариант 1: время в секундах:
r.setex('some_key1', 100500, 'first value')
# Вариант 2: время в целевых единицах:
r.setex('some_key2', timedelta(minutes=100500), 'second value')
# Так же есть методы установки expires ключа по метке timestamp и datetime.

print('some_key1: ' + r.get('some_key1').decode('utf-8'))
print('some_key2: ' + r.get('some_key2').decode('utf-8'))

sleep(1)
print('TTL some_key1 (seconds):' + str(r.ttl('some_key1')))
print('TTL some_key2 (milliseconds):' + str(r.pttl('some_key2')))

# Изменить expire ключей.
r.expire('some_key1', 1)
r.expire('some_key2', timedelta(seconds=1))

# Проверить сужествование ключа.
print(f'is some_key1 exists?: {r.exists("some_key1")}')
print(f'is some_key2 exists?: {r.exists("some_key2")}')

sleep(1)

# Выбрасывается исключение:
# AttributeError: 'NoneType' object has no attribute 'decode'
print('some_key1: ' + r.get('some_key1').decode('utf-8'))
if r.exists("some_key2"):
    print('some_key2: ' + r.get('some_key2').decode('utf-8'))