num_lim=-1
jilst=[]

zen_suu='０１２３４５６７８９'
kan_suu='０一二三四五六七八九'

while True:
    mojir=input()
    if mojir=='':
        break

    hyo=mojir.split(' ')
    suu=int(hyo[1])
    if suu > num_lim:
        num_lim=suu//100*100+99
        delim=''
        if suu//100%10==0:
            delim+=zen_suu[suu//1000]
            print(delim+'-')            
        else:
            delim+=kan_suu[suu//100%10]
            print('-'+delim)

    #print(mojir)
    print(hyo[0])
