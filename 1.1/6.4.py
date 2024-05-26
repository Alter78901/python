
def fh(s,x):
    count = 0
    for char in s:
        if char == x:
            count += 1
    return count

s='hello woeld'
x='l'
print(f'{s}里面有{fh(s,x)}个"{x}"')