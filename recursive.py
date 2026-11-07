n = int(input())

tab = [0] * (n+1)

tab[1] = 1

for i in range(2,n+1):
    tab[i] = 1 + tab[i - tab[tab[i-1]]]

print(tab[n])