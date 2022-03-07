#najdu nejmenší prvek a prohodím s prvním prvek, posunu za něj indikátor setříděné části seznamu
#najdu další nejmenší, prohodím s prvkem za indikátorem, ten zas posunu

alist = ['b', 'e','k','f', 's']

ind = 0
min = alist[0]
x = ''
idx = 0

while ind < len(alist):
    i = 0
    for element in range(ind,len(alist)):
        if alist[element] < min:
            min = alist[element]
            idx = i
        i += 1
    #x = alist[ind]
    #alist[ind] = alist[idx]
    #alist[idx] = x
    ind += 1
    print(min)


print(alist)
