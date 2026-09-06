import re

hsd_dir='./hasida-table'

with open(hsd_dir+'/aiueo-full-1351_utf8.txt') as f:
    tcode_moji=f.read()

while True:
    mojir=input()
    if mojir=='':
        break

    hyo=mojir.split(',')

    moji=hyo[0][0] #nice Unicode
    ate=re.search('[0-9]+',hyo[7])
    suu=ate[0]

    if moji in tcode_moji: #so fast!!
        print(f'{suu} {moji}')
    
