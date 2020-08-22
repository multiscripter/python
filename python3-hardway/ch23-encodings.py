import sys

script, enc, err = sys.argv

def main(langFile, enc, errors):
	line = langFile.readline()

	if line:
		printLine(line, enc, errors)
		return main(langFile, enc, errors)

def printLine(line, enc, errors):
	nextLang = line.strip()
	encoded = nextLang.encode(enc, errors = errors)
	decoded = encoded.decode(enc, errors = errors)

	print(f"""
{nextLang}
{encoded}
{decoded}""")

langs = open("ch23-languages.txt", "r", -1, enc)

main(langs, enc, err)

print("=======================================")
uni = b'\xd0\xa3\xd0\xba\xd1\x80\xd0\xb0\xd1\x97\xd0\xbd\xd1\x81\xd1\x8c\xd0\xba\xd0\xb0'
uni = uni.decode("utf-8")
print(uni)

# Запуск: python ch23-encodings.py utf-8 strict