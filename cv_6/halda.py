def lchld(me: int):
    return me*2

def rchld(me: int):
    return me*2+1

def parent(me: int):
    return me//2

def insert(heap: list, item):
    heap.append(item)
    fixUp(heap)

def swap(heap: list, idx_parent: int, idx_chld: int):
    temp = heap[idx_parent]
    heap[idx_parent] = heap[idx_chld]
    heap[idx_chld] = temp

def fixUp(heap):
    idx = len(heap)-1

    #dokud nejsem v kořeni
    while idx > 1:
        #podívám se na rodiče, pokud je menší než já, končím
        rodic = heap[parent(idx)] 
        if rodic < heap[idx]:
            return

        #podívám se jestli, jsem pravý nebo levý potomek
        if idx%2 == 0:
            idx_chld = idx + 1
            if idx_chld > len(heap)-1: #pokud na začátku přiřadím do levého potomka, pravý neexistuje a idx_chld vyteče z haldy, tak prohodím rovnou
                swap(heap, parent(idx), idx)
                idx = parent(idx)
                continue
        else:
            idx_chld = idx - 1
        
        #kouknu, který z potomků je menší a ten prohodím s rodičem
        if heap[idx] <= heap[idx_chld]:
            swap(heap, parent(idx), idx)
        else: 
            swap(heap, parent(idx), idx_chld)
        
        #posunu se na pozici rodiče
        idx = parent(idx)

heap = [0, 1, 3, 5, 6, 4, 10, 11, 16, 20, 9]
insert(heap, 2)
insert(heap, 3)
print(heap)

#fixUp
    #dokud nejsem v kořeni
        #podívám se na rodiče
        #pokud rodič je menší než já, končím
        #jinak
            #prohodím rodiče s menším ze synů
            #posunu se na pozici rodiče
