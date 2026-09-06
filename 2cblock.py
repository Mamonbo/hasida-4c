num_lim=-1
jilst=[]

zen_suu='０１２３４５６７８９'
kan_suu='０一二三四五六七八九'

while True:
    mojir=input()
    if mojir=='':
        break

    hyo=mojir.split(' ')
    suu=int(hyo[0])
    if suu > num_lim:
        num_lim=suu//1000*1000+999
        delim=''
        if suu//1000%10==0:
            delim+=zen_suu[suu//10000]
            print(delim+'-')            
        else:
            delim+=kan_suu[suu//1000%10]
            print('-'+delim)

    #print(mojir)
    print(hyo[1])
