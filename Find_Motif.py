import re
def tablicaPrefiksowa(wzorzec):
    m = len(wzorzec)
    P = []
    P.insert(0,0)
    P.insert(1,0)
    k = 0
    for q in range(1, m): 
        while k > 0 and wzorzec[k] != wzorzec[q]:
            k = P[k]
        if wzorzec[k] == wzorzec[q]:
            k = k + 1
        P.insert(q+1,k)   
    return P

def AlgorytmKMP(txt,wzorzec):
    found = []
    m = len(wzorzec)
    n = len(txt)
    P = tablicaPrefiksowa(wzorzec)
    q = 0
    i = 0
    while i <= (n-m):
        q = P[q]
        while q < m and (wzorzec[q] == txt[i+q]):
            q = q + 1
        if q == m:
            found.append(i+1)
        i = i + max(1, q-P[q])
    return found

if __name__ == '__main__':
    wzorzec = 'CTGGCCTCT'
    with open("rosalind_subs.txt",'r') as file:
        txt = file.read()
        print(AlgorytmKMP(txt,wzorzec))

      
    
