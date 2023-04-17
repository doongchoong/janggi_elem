import os
import base64

# 이미지를 BASE64로 변경


d = os.path.dirname(__file__)
print(d)

p = d + '/imgs/'

ddd = {
'blue_advisor.png' : 'A',
'blue_cannon.png' : 'C',
'blue_chariot.png' : 'R',
'blue_elephant.png' : 'E',
'blue_horse.png' : 'N',
'blue_king.png' : 'K',
'blue_pawn.png' : 'P',
'red_advisor.png' : 'a',
'red_cannon.png' : 'c',
'red_chariot.png' : 'r',
'red_elephant.png' : 'e',
'red_horse.png' : 'n',
'red_king.png' : 'k',
'red_pawn.png' : 'p',
}


ret_str = ''

for k,v in ddd.items():
    path = p + k
    with open(path, 'rb') as img:
        ret_str += "'" + v + "': 'data:image/png;base64,"+ base64.b64encode(img.read()).decode() + "',\n"

with open('output.txt', 'w') as f:
    f.write(ret_str)

