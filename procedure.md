# clone hasida-table
`git clone https://github.com/makoto-fujiwara/hasida-table.git`

# aiueo-full-1351_utf8.txt
convert the coding of aiueo-full-1351.jis

from ISO-2022 to UTF-8

`nkf hasida-table/aiueo-full-1351.jis -u > hasida-table/aiueo-full-1351_utf8.txt`

# 2c_linewise.txt (from chinese-japanese dic)
`python3 filter_cn.py <chinadat.csv |uniq |sort -n |python3 2cblock.py > 2c_linewise.txt`

speed issue is fixed with the power of python

ignore EOF errors

# 2c.jis
convert ISO-2022-jp for hasida-table

`cat 2c_linewise.txt |tr -d '\n'|tr  '-' '\n' |nkf -j > 2c.jis`

# 2c.ps and 2c.pdf
using hasida-table

see [https://gist.github.com/Mamonbo/2bf4d9e3baa4b2ebec3a6b9b07e176fe](here)

`./hasida-table/hasida-table -s ./hasida-table/tcode.st -b -o 2c.jis >2c.ps
`

