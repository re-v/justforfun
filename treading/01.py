import threading
import time
from datetime import datetime

def fun1():
    print('start fun!  at:' + time.ctime())
    time.sleep(4)
    print('end fun')

def fun2():
    print('start fun2!')
    time.sleep(5)
    print('end fun2')

def main():
    t1 = threading.Thread(target=fun1,args=())
    t1.start()
    t1.join()

    t2 = threading.Thread(target=fun2, args=())
    t2.start()
    t2.join()

if __name__ == '__main__':
    main()
    print('ok')