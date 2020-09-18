import datetime
import redis

# https://python-scripts.com/redis

r = redis.Redis()
r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})
val = r.get("Bahamas")
print(val.decode("utf-8"))

today = datetime.date.today()
print(today.isoformat())
visitors = {"dan", "jon", "alex"}
# В redis-py ключами могут быть только bytes, str, int или float.
# Сам Redis конвертит их в байты.
# Добавить множество (Set) по ключу строковой даты:
r.sadd(today.isoformat(), *visitors)
