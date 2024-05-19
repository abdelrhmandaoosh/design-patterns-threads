import time 
def calc_square(numbers):
    print("calculate squaer numbers\n")
    for n in numbers:
        print('square' , n*n,'\n')
        time.sleep(0.2)


def calc_cube(numbers):
    print("calculate cube numbers\n")  
    for n in numbers:
        print("cube", n*n*n,'\n' )
        time.sleep(0.2)   

x=[2,3,8,4]
t=time.time()
calc_square(x)
calc_square(x)
print("done in :" ,time.time()-t )   
              