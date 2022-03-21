def insert(heap: list, item):
    heap.append(item)
    fixUp(heap)

def fixUp(heap):
    idx = len(heap)-1
    while idx > 1:
        pass 

def lchld(me: int):
    return me*2

def rchld(me: int):
    return me*2+1

def parent(me: int):
    return me//2


#fixUp
    #dokud nejsem v kořeni
        #podívám se na rodiče
        #pokud rodič je menší než já, končím
        #jinak
            #prohodím rodiče s menším ze synů
            #posunu se na pozici rodiče
