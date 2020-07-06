import requests

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'

r = requests.get(url)
text = str(r.content)

file = open('output.txt','w')
file.write(str(text))
file.close()