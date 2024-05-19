import time
import concurrent.futures
def calc_square(numbers):
    print("calculate square numbers \n")
    for n in numbers:
        print("square", n*n ,'\n')
        time.sleep(2)

def calc_cube(numbers):
    print("calculate cube numbers \n")
    for n in numbers:
        print("cube", n*n*n ,'\n')
        time.sleep(2)
y=[2,3,8,7]        

pool= concurrent.futures.ThreadPoolExecutor(max_workers=2)
pool.submit(calc_square , y)
pool.submit(calc_cube , y)
pool.shutdown(wait=True)
print("main thread continuing to run")        