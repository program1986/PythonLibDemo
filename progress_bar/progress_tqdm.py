#from tqdm import tqdm,trange
#from tqdm.tk import tqdm,trange
from tqdm import tqdm
from time import sleep

X=10000

def tqdm_test():
    for i in tqdm(range(X)):
        for j in range(X):
            k=j*i
    print('\nDone')    

def trange_test():
    for i in trange(X):
        for j in range(X):
            k=j*i
    
    print('\nDone')

def progress_test():
    bar = tqdm(total=100)
    bar.set_description('Step1:')
    sleep(0.5)
    bar.update(10)

    bar.set_description('Step1:')
    sleep(0.5)
    bar.update(10)

    bar.set_description('Step2:')
    sleep(0.5)
    bar.update(10)

    bar.set_description('Step3:')
    sleep(0.5)
    bar.update(10)
        
    bar.set_description('Step4:')
    sleep(0.5)
    bar.update(10)

    bar.set_description('Step5:')
    sleep(0.5)
    bar.update(50)

    print('\nDone')

if __name__=="__main__":
    #tqdm_test()
    #trange_test()
    progress_test()