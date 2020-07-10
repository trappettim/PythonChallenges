import requests
import pickle
import pandas as pd
desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',30)

url = 'http://www.pythonchallenge.com/pc/def/banner.p'

r = requests.get(url)
webpage = r.content

file = open('Challenge5', 'wb')
file.write(webpage)
file.close()

infile = open('Challenge5', 'rb')
solution = pickle.load(infile)
infile.close()

df = pd.DataFrame(solution)
print(df)

for row in solution:
    print('')
    for i,ch in enumerate(row):
        print(ch[0]*ch[1],end='')
