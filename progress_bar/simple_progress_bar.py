# simple processbar
X = 10000
for i in range(X):
    for j in range(X):
       k = i * j
    print ('processing:',
           f'|{"#"*((i+1)*50//X):50}|',
           f'{(i+1)*100//X}%',
           end='\r')

print ('\nDone!')


'''
process: |##################################################| 100%
Done!
'''
