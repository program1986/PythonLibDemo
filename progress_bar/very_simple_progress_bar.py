# very simple processbar
X = 10000
for i in range(X):
    for j in range(X):
       k = i * j
    print (f'{i+1}/{X}',end='\r')

print ('\nDone!')


