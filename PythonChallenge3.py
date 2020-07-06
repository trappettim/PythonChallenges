import requests

url = 'http://www.pythonchallenge.com/pc/def/equality.html'

r = requests.get(url)
text = str(r.content)

# file = open('output.txt','w')
# file.write(str(book))
# file.close()

solution=''

for index in range(0,len(text)):
    if text[index].islower():
        if text[index+1].isupper():
            if text[index+2].isupper():
                if text[index+3].isupper():
                    if text[index+4].islower():
                        if text[index+5].isupper():
                            if text[index+6].isupper():
                                if text[index+7].isupper():
                                    if text[index+8].islower():
                                        solution=''.join([solution,text[index+4]])
                                        print(solution)
    

