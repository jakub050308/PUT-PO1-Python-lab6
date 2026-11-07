import sys
sys.setrecursionlimit(1000000)

n = int(input())

def visit(g, h):
    global n

    if g<0 or g>=n or h<0 or h>=n:
        return

    if sea[g][h] == 0:
        return

    sea[g][h] = 0
    visit(g-1,h)
    visit(g+1,h)
    visit(g,h-1)
    visit(g,h+1)




sea = []

for _ in range(n):
    sea.append(list(map(int,input())))

count = 0

#if sea[0][0] == 1:
#    count += 1
#    sea[0][0] = -1

#for i in range(1, n):
#    if sea[0][i-1] == -1 and sea[0][i] == 1:
#        sea[0][i] = -1
#    if sea[0][i-1] == 0 and sea[0][i] == 1:
#        count += 1
#        sea[0][i] = -1


#for i in range(1, n):
#    if sea[i-1][0] == -1  and sea[i][0] == 1:
#        sea[i][0] = -1
#    if sea[i-1][0] == 0 and sea[i][0] == 1:
#        count+= 1
#        sea[i][0] = -1

#for i in range(1,n):
#    for j in range(1,n):
#        if (sea[i-1][j] == -1 or sea[i][j-1] == -1) and sea[i][j] == 1:
#            sea[i][j] =-1
#        if sea[i-1][j] == 0 and sea[i][j-1] == 0 and sea[i][j] == 1:
#            sea[i][j] = -1
#            count += 1

#for i in range(1, n):
#    for j in range(1, n):
#        if (sea[i-1][j] == -1 or sea[i+1][j] == -1 or sea[i][j-1] == -1 or sea[i][j+1] == -1) and sea[i][j] == 1:
#            sea[i][j] = -1

#print(count, end="\n\n")
#for i in range(n):
#    for j in range(n):
#        print(sea[i][j], end=" ")
#    print("\n")


for i in range(n):
    for j in range(n):
        if sea[i][j] == 1:
            count += 1
            visit(i,j)

print(count)