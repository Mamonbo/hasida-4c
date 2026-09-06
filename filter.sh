hsd_dir="./hasida-table"

while true;do
    read suu mj
    if echo $suu |grep ';' --silent;then
	continue
    fi
    if test -z $mj;then
	break
    fi
    #echo $mj
    moji=$(echo $mj|tr -d '/')
    #echo $moji

    if test $(echo $suu |wc -c) -gt 5;then #ignore 5 digits
	continue
    fi
    if  grep $moji $hsd_dir/aiueo-full-1351_utf8.txt --silent;then
	echo $moji $suu
    fi
done
echo ''
