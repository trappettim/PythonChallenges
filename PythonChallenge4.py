import requests
import numpy as np
import pandas as pd

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'

r = requests.get(url)
text = str(r.content)

# file = open('output.txt','w')
# file.write(str(text))
# file.close()

index = text.find('nothing')
code = '12345'
# code_list = ['97034', '23939', '97640', '41703', '23323', '21133', '36426', '56197', '8804', '39851', '1266', '43183',
#              '13144', '77178', '25292', '86154', '57132', '17394', '38000', '14833', '56920', '19603', '54071', '67328',
#              '71306', '84441', '16263', '5283', '4322', '14095', '58995', '33155', '30436', '36716', '99377', '92526',
#              '66228', '49620', '2083', '23208', '49606', '50373', '38162', '20408', '3579', '86236', '45610', '91947',
#              '66007', '28967', '90487', '42571', '80694', '81706', '99478', '11480', '41847', '33856', '2776', '58397',
#             '52459', '96142', '56577', '27335', '53166', '84164', '39174', '39115', '74770', '27075', '85259', '81597',
#              '43365', '36077', '48826', '96682', '58874', '47102', '61950', '84673', '80398', '23228', '16839', '48100',
#              '78189', '57274', '55873']

code_list = []
code_int_list = []

for cd in code_list:
    code_int_list.append(int(cd))

def get_page_html(page_code):
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + page_code
    r = requests.get(url)
    return str(r.content)


def get_new_code(old_code):
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + old_code
    r = requests.get(url)
    page_text = str(r.content)
    return page_text[26:-1]


for i in range(0, 400):
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + code
    r = requests.get(url)
    page_text = str(r.content)
    index = page_text.find('nothing is')
    code = page_text[index + 10:-1]
    print(str(i) + ' ' + code + ' ' + page_text)
    if code in code_list:
        break
    elif len(get_page_html(code)) > 32:
        pass
    else:
        code_list.append(code)

# file = open('codelist.txt', 'w')
# file.write(str(code_list))
# file.close()

# code_array = np.array(code_int_list)
code_series = pd.Series(code_int_list)
print(code_series.describe())

'''to check specific code html scripts'''
# code = '55873'
# url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + code
# r = requests.get(url)
# page_text = str(r.content)
# file = open('codelist{}.txt'.format(code), 'w')
# file.write(page_text)
# file.close()
