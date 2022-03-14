from statistics import median


alist = ["c","a", "x", "t", "c", "c", "v", "b", "s","c"]
'''
def prohod (alist: list, l: int, r: int, pivot):
    while r-l >= 1:
        while alist[l] <= pivot:
            l += 1
        while alist[r] > pivot:
            r -= 1
        if r-l >= 1:
            temp = alist[l]
            alist[l] = alist[r]
            alist[r] = temp
    return l, r 
'''

def prohod (alist: list, l: int, r: int, pivot):
    i = l
    j = r
    while i < j:
        while alist[i] < pivot:
            i += 1
        while alist[j] > pivot:
            j -= 1
        if i > j:
            return i, j
        temp = alist[i]
        alist[i] = alist[j]
        alist[j] = temp
        i+=1
        j-=1
    return i, j 

def quick_sort (alist: list, l: int, r: int):    
    if r-l <= 1:
        return alist
    pivot = alist[int((l+r)/2)]
    m,n = prohod(alist, l, r, pivot)
    print(m,n,l,r)
    quick_sort(alist, l, n)
    quick_sort(alist, m, r)


sorted_list = quick_sort(alist, 0, len(alist)-1)
print(sorted_list)
#prohod(alist, 0, len(alist)-1, "c")
#print(alist)      