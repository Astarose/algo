from random import randint

tab_min = 0
tab_max = 100
tab_length = randint(tab_min, tab_max)
tab = []

for k in range(tab_length):
    tab.append(randint(tab_min, tab_max))

tab.sort()
print(tab)
