import requests
import collections
from collections import Counter

url = 'http://www.pythonchallenge.com/pc/def/ocr.html'

r = requests.get(url)
book = str(r.content)
index = book.find('below:')
book = book[index+21:]
# file = open('output.txt','w')
# file.write(str(book))
# file.close()

char_counter = Counter(book)
print(''.join(list(char_counter.keys())[-11:-3]))
      