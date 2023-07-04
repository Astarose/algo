from random import randint

tab_min = 0
tab_max = 99
tab_length = randint(tab_min, tab_max)
number = randint(tab_min, tab_max)
tab = []

for k in range(tab_length):
    tab.append(randint(tab_min, tab_max))
    tab.sort()

tab_left = []
tab_right = tab

for i in range(len(tab)//2):
    tab_left.append(tab[i])
    tab_right.pop(i)

print(tab_left, tab_right)
