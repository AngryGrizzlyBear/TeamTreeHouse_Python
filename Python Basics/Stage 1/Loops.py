names = ['Kenneth', 'Stacy', 'Tupac', 'QUIT', 'Stan' ]

for name in names:
    if name == 'QUIT':
        break
    print(name)

for name in names:
    if name == 'QUIT':
        continue
    print(name)    