import datetime
from pprint import pprint
import pymongo
from pymongo import MongoClient

# Настройки сервера лежат в файле /etc/mongod.conf

# https://api.mongodb.com/python/current/api/
# https://pymongo.readthedocs.io/en/stable/tutorial.html

# Подключиться кконкретному хосту и порту.
# client = MongoClient('ip_address_or_symbolic_name', port_number)
# ip_address_or_symbolic_name (127.0.0.1 или mongodb-server.domain)
# port_number вида XXXXX, например 27017.

# Подключиться к хосту и порту по умолчанию: 127.0.0.1:27017
from pymongo.errors import DuplicateKeyError

client = MongoClient()

# Подключиться к БД 'mongodb_tutorial'.
db = client.mongodb_tutorial

# Если имя БД имеет символы, не позволяющие обратиться к ней как к атрибуту,
# то получить доступ можно через нотацию словаря.
# db = client['mongodb-tutorial']

# Получить коллекцию (аналогично получению БД).
posts = db.posts

print(db.list_collection_names())

# Данные в MongoDB представлены (и хранятся) с использованием документов в стиле JSON.
# В PyMongo мы используем словари для представления документов.
td_now = datetime.datetime.utcnow()
post = {
    'author': 'Foo',
    'text': 'Some cool text',
    'tags': ['mongodb', 'python', 'pymongo'],
    'date': td_now
}
# Python типы вроде datetime автоматом конвертируются в BSON и обратно.

# Вставить документ в БД и вернуть сгенерированный id.
persisted = posts.insert_one(post)
print(persisted.inserted_id)

# Множественная вставка.
new_posts = [
    {'author': 'Bar', 'text': 'Bar-text'},
    {'author': 'Baz', 'text': 'Baz-text'}
]
result = posts.insert_many(new_posts)
print(result.inserted_ids)

# Получить (случайный?) документ.
# found = posts.find_one()
# Найти документ по фильтру (например дате).
pprint(posts.find_one({'date': td_now}))
# Найти по ID.
# В mongoDB ID - это объект, а не строка!
# Если есть ID в виде строки, то его нужно сконвертировать так ObjectId(str_id)
pprint(posts.find_one({'_id': persisted.inserted_id}))

# Получить все документы.
# Метод find() возвращает курсор итератора.
retrieved = posts.find()
# Получить из курсора количество элементов.
print(retrieved.count()) # count is deprecated. Use Collection.count_documents instead.
# Для получения количества документов в коллекции есть специальный метод.
print(posts.count_documents({}))
# Получить количество по фильтру.
print(posts.count_documents({'author': 'Foo'}))

# Поиск по фильтру.
filtered = posts.find({'author': 'Bar'})
print(filtered)
print(posts.count_documents({'author': 'Bar'}))

# Поиск по условию.
# https://pymongo.readthedocs.io/en/stable/api/pymongo/cursor.html#pymongo.cursor.Cursor.sort
bar_posts = posts.find({'author': {'$eq': 'Bar'}}).sort([('date', pymongo.DESCENDING)])
for bar_post in bar_posts:
    pprint(bar_post)

# Индексы.
# MongoDB автоматически создаёт индекс для поля _id
# Создать коллекцию "Профили".
profiles = db['profiles']
# Удалить всё из коллекции.
profiles.delete_many({})
# Созадть индекс для поля user_id. Ограничения: уникальность.
index_res = profiles.create_index([('user_id', pymongo.ASCENDING)], unique=True)
user_profiles = [
    {'user_id': 211, 'name': 'Luke'},
    {'user_id': 212, 'name': 'Ziltoid'}
]
result = db.profiles.insert_many(user_profiles)
duplicate_profile = {'user_id': 212, 'name': 'Tommy'}
try:
    db.profiles.insert_one(duplicate_profile)
except DuplicateKeyError as ex:
    print(ex.__str__())

print(posts.delete_many({}))