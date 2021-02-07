a = [234, 543, 394]
print(a)
for thing in a:
    print(thing)
c = []
for i in range(3):
    b = a[i]
    print('before' , i, b, c)
    print (b % 2)
    if b % 2 == 0:
        c.append(b)
    print('after' , i, b, c)
    print('- ' *20)
    # for i in range(12):
    #     if i % 3 == 0:
    #         print(i, 'i is divisible by 3')
    #     else: 
    #         print(i , 'DOH')

for x in range(3):
    for y in range(3):
        print(x, y)
    print( 'x, y' , x*y)


print('whatup')
