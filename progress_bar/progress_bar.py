# pip install progress

from progress.bar import Bar
X = 10000
with Bar('Processing', max=X) as bar:
    for i in range(X):
        for j in range(X):
            k = i * j
        bar.next()
print ('\nDone!')


'''
Processing |################################| 10000/10000

Done!
'''

