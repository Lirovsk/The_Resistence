um = [2, 0, None]
nomes = []
for i in range(0,5):
    nomes.append(input())
print ("\n")
for i in nomes:
    if nomes.index(i) not in um:
        print(i, end= "   ")
