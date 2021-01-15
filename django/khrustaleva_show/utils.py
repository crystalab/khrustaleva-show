from django.utils.text import slugify
from time import time
import requests

def create_slug(s):
	translit = {
		'а': 'a',
		'б': 'b',
		'в': 'v',
		'г': 'g',
		'д': 'd',
		'е': 'e',
		'ё': 'e',
		'ж': 'zh',
		'з': 'z',
		'и': 'i',
		'й': 'y',
		'к': 'k',
		'л': 'l',
		'м': 'm',
		'н': 'n',
		'о': 'o',
		'п': 'p',
		'р': 'r',
		'с': 's',
		'т': 't',
		'у': 'u',
		'ф': 'f',
		'х': 'kh',
		'ц': 'c',
		'ч': 'ch',
		'щ': 'shch',
		'ш': 'sh',
		'ь': '',
		'ы': 'i',
		'ъ': '',
		'э': 'a',
		'ю': 'yu',
		'я': 'ya',
	}

	i = 0
	s.lower()
	s = slugify(s, allow_unicode=True)
	for letter in s:
		length = len(s)
		key = ord(letter)
		if key >= 1072 and key <= 1105:
			s = s[:i] + translit[letter] + s[i+1:]
		i += len(s) - length + 1
	new_slug = s + str(int(time()))
	return new_slug

def sendToTelegram(text: str):
	token = "1227162866:AAFwhGLni1TwCHeMbqL3BMRE8JPn530Rsh0"
	url = "https://api.telegram.org/bot"
	channel_id = "-1001280588110"
	url += token
	method = url + "/sendMessage"

	r = requests.post(method, data={"chat_id": channel_id, "text": text})

	if r.status_code != 200:
		raise Exception("post_text error")

