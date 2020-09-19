import redis
import random

# Магазин эксклюзивных шляп.

hats_list = [
    {
        "color": "black",
        "price": 49.99,
        "style": "fitted",
        "quantity": 1,
        "purchased": 0,
    },
    {
        "color": "maroon",
        "price": 59.99,
        "style": "hipster",
        "quantity": 5,
        "purchased": 0,
    },
    {
        "color": "green",
        "price": 99.99,
        "style": "baseball",
        "quantity": 2,
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
    # В отличие от save(), этот метод является асинхронным
    # и немедленно возвращается.
    r.bgsave()

# Python 3 не поддерживает обращение к keys() по индексу.
first_key = list(hats_dict.keys())[0]
# Получить шляпу по ключу.
print(r.hgetall('hat:1326692461'))
print(r.hgetall(first_key))


def buy_item(r: redis.Redis, item_id: int) -> None:
    """Функция покупки шляпы показывается, как избежать условия гонки
    в случае попытки двух пользователей купить последнюю шляпу.
    Redis реализует optimistic locking.
    Командой WATCH (метод watch() redis-py) Redis блокирует значение по ключу
    и наблюдает не пытаются ли другие потоки изменить значение по ключу.
    Если попытка происходит, вызываемая функция просто повторяет
    весь процесс заново."""

    # Создать новый объект конвейера, который может пыстроить в очередь
    # несколько команд для последующего выполнения.
    with r.pipeline() as pipe:
        error_count = 0
        while True:
            try:
                # Перехватить блокировку и начать наблюдение.
                pipe.watch(item_id)
                # Получить количество в переменную n_left типа bytes.
                n_left: bytes = r.hget(item_id, "quantity")
                if n_left > b'0':
                    # После вызова команы WATCH вызвать метод multi()
                    # который установит начало транзакции.
                    pipe.multi()
                    # Уменьшить quantity на 1.
                    pipe.hincrby(item_id, 'quantity', -1)
                    # Увеличить purchased на 1.
                    pipe.hincrby(item_id, 'purchased', 1)
                    # Выполнить все команды транзакции в текущем конвейере.
                    pipe.execute()
                    break
                else:
                    # Снять блокировку и остановить наблюдение значения.
                    pipe.unwatch()
                    raise OutOfStockException(
                        f"Sorry, {item_id} is out of stock!"
                    )
            except redis.WatchError:
                # Регистрация общего количества ошибок данного пользователя,
                # с последующей попыткой повторения
                # процесса WATCH/HGET/MULTI/EXEC
                error_count += 1
    return


class OutOfStockException(Exception):
    """Пользовательское исключение 'Распродано'."""
    pass
