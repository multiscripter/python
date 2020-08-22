import smtplib # SMTP protocol client (requires sockets).
# https://docs.python.org/3/library/smtplib.html#module-smtplib
# Source code: https://github.com/python/cpython/tree/3.8/Lib/smtplib.py

# Модуль smtplib определяет объект сеанса клиента SMTP, 
# который можно использовать для отправки почты на любой компьютер 
# в Интернете с помощью демона прослушивателя SMTP или ESMTP.

try:
	server = smtplib.SMTP('localhost')
	server.set_debuglevel(1)
	server.sendmail('admin@bot.net', 'ill-jah@yandex.ru', """
Hello! This is a test email from python. Thanks.
		""")
	server.quit()
except Exception as ex:
	print(ex)
#print(server)

# Короч чтобы всё заработал нужно поставить у себя почтовый сервер,
# либо побключаться к чужим со своими логином и паролем.