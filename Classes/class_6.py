fruits = ['apple', 'orange', 'pear']
animals = ['dog', 'cat', 'horse']

for f in fruits:
    print(f)

for a in animals:
    print(a)

# O (2+F+A)   2 is a constant = our 2 lists. We can remove constant
print('----------')

for a in animals:
    for f in fruits:
        print(f'{a} eats {f}')


num = len (animals)
while num > 0:
    print(num)
    num -= 1
    for a in animals:
        print(f'{num} ---{a}')
    for f in fruits:
        print(f'{num} ----{f}')
# O (A*(A+F))

print('----------')
for a in animals:
    print(a)
u =0
while u<len(animals):
    print(u)
    u+=1

# O(A+A) = O(A)

def counter (num):
    print(num)
    if num>0:
        counter (num-1)

counter (3)






