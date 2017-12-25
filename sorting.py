def bubble_sort(L):
    if not L: return []
    clear = False
    while not clear:
        clear = True
        for i in range(len(L)-1):
            if L[i]>L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                clear = False
        
def insertion_sort(L):
    if not L: return []
    for i in range(1, len(L)):
        pos = i-1
        key = L[i]
        while L[pos] > key and pos >=0:
            L[pos+1] = L[pos]
            pos-=1
        L[pos+1] = key
        
def selection_sort(L):
    if not L: return []
    for i in range(len(L)):
        m = min(range(i,len(L)), key=lambda x: L[x])
        L[i], L[m] = L[m], L[i]
