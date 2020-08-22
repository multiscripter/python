import urllib.request # Extensible library for opening URLs.
# https://docs.python.org/3/library/urllib.request.html#module-urllib.request
# Source code: https://github.com/python/cpython/tree/3.8/Lib/urllib/request.py

# Модуль urllib.request определяет функции и классы, которые помогают 
# открывать URL-адреса (в основном HTTP) в сложном мире 
# - базовая и дайджест-аутентификация, перенаправления, файлы cookie и многое другое.

# urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
# Откройте URL-адрес, который может быть строкой или объектом Request.
# Возвращает объект класса http.client.HTTPResponse(sock, debuglevel=0, method=None, url=None)
# https://docs.python.org/3/library/http.client.html#httpresponse-objects
urlopen = urllib.request.urlopen
ctx = urlopen('http://podillbot.3141.ru/videos/videos.txt')
print(ctx) # <http.client.HTTPResponse object at 0x7f1b961be668>
print()

print('ctx.read():', ctx.read()) # Читает всё содержимое.
print('ctx.getheaders():', ctx.getheaders())
print('ctx.closed:', ctx.closed)
print()

for k in ctx.__dict__:
	print(f'{k}: {getattr(ctx, k)}')