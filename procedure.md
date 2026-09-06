# clone hasida-table
`git clone https://github.com/makoto-fujiwara/hasida-table.git`

# aiueo-full-1351_utf8.txt
convert the coding of aiueo-full-1351.jis

from ISO-2022 to UTF-8

`nkf hasida-table/aiueo-full-1351.jis -u > hasida-table/aiueo-full-1351_utf8.txt`

# 2c_linewise.txt (from SKK dic)
`cat SKK_JISYO.shikakugoma |bash filter.sh |python3 2cblock.py > 2c_linewise.txt`

it takes 1 minute or so because grep is called so many times
in filter.sh

it remains unfixed because genarating hasida table is not
so much in the life

# 2c.jis
convert ISO-2022-jp for hasida-table

`cat 2c_linewise.txt |tr -d '\n'|tr  '-' '\n' |nkf -j > 2c.jis`

# 2c.ps and 2c.pdf
using hasida-table

see [https://gist.github.com/Mamonbo/2bf4d9e3baa4b2ebec3a6b9b07e176fe](here)

`./hasida-table/hasida-table -s ./hasida-table/tcode.st -b -o 2c.jis >2c.ps
`

