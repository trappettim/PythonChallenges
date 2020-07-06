file = open('Challenge1.txt','r')
f = file.readlines()
sentence = f[8][30:-1]
# alphabet = 'xyzabcdefghijklmnopqrstuvwxyz'
# sentence = list(sentence)
# for i,ch in enumerate(sentence):
#     if ch == ' ' or ch == '.' or ch == '(' or ch == ')':
#         pass
#     else:
#         index = alphabet.find(sentence[i])
#         index = index + 2
#         sentence[i] = alphabet[index]
# print (''.join(sentence))

alphabet = 'abcdefghijklmnopqrstuvwxyz'
newalphabet = 'yzabcdefghijklmnopqrstuvwx'

trantab = str.maketrans(newalphabet,alphabet)
print(sentence.translate(trantab))

url = 'http://www.pythonchallenge.com/pc/def/map.html'

print (url.translate(trantab))