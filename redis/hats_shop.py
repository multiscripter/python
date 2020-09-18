import random

import redis

# Магазин эксключивных шляп.

hats_list = [
    {
        "color": "black",
        "price": 49.99,
        "style": "fitted",
        "quantity": 1000,
        "purchased": 0,
    },
    {
        "color": "maroon",
        "price": 59.99,
        "style": "hipster",
        "quantity": 500,
        "purchased": 0,
    },
    {
        "color": "green",
        "price": 99.99,
        "style": "baseball",
        "quantity": 200,
        "purchased": 0,
    }
]
random.seed(444)
# Использование префикса hat: является соглашением Redis
# для создания своеобразного пространства имен внутри базы данных.
# Хэш содержит ключ с префиксом случайного числа. Например: hat:56854717.
hats_dict = {f'hat:{random.getrandbits(32)}': hat for hat in hats_list}

# Создать БД с номером 1.
r = redis.Redis(db=1)

# Вернуть новый объект конвейера, который может поставить в очередь
# несколько команд для последующего выполнения.
with r.pipeline() as pipe:
    for hat_id, hat in hats_dict.items():
        # Устанавливает для указанных полей соответствующие
        # значения в хэше, хранящемся в ключе.
        pipe.hmset(hat_id, hat)
    # Выполнить все команды в текущем конвейере.
    pipe.execute()
    # Сказать серверу Redis сохранить данные на диск.
    # В отличие от save (), этот метод является асинхронным
    # и немедленно возвращается.
    r.bgsave()

# Python 3 не поддерживает обращение к keys() по индексу.
first_key = list(hats_dict.keys())[0]
# Получить шляпу по ключу.
print(r.hgetall('hat:1326692461'))
print(r.hgetall(first_key))
