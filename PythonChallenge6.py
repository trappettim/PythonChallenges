import zipfile

readmefile = open('Challenge6/readme.txt', 'r')
print(readmefile.read())

archive = zipfile.ZipFile(r'Challenge6\channel.zip', 'r')

comments=[]

nothing = '90052'
for i in range(1, 1000):
    file = open('Challenge6/{}.txt'.format(nothing), 'r')
    text = file.read()
    comment = str(archive.getinfo(nothing + '.txt').comment)
    comments.append(comment[2:-1])
    if text.find('nothing is ') != -1:
        index = text.find('nothing is ')
        nothing = text[index+11:]
        print(str(i) + ' ' + text + ' ' + nothing)
    else:
        print(text)
        break

print(comments)
for ch in comments:
    if ch == '\\n':
        print('')
    else:
        print(ch, end='')