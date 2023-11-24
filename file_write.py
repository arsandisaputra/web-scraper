import os

data = ['a', 'b', 'c']
with open('tes_write.txt', 'w') as file:
    for d in data:
        w = d + "\n"
        file.write(w)
