from threading import Thread
import threadfunction
import time
import vars
import config


def main():
   #https://morvanzhou.github.io/tutorials/python-basic/threading/3-join/
   # About how to join
   t1=Thread(target=threadfunction.threadfunction1,args=())
   t2=Thread(target=threadfunction.threadfunction2,args=())
   t3=Thread(target=threadfunction.killMain,args=())
   t1.daemon=True
   t2.daemon=True
   t3.daemon=True
   t1.start()
   t2.start()
   t3.start()
   print("main, value a in config as " + str(config.a)  )  
   while not vars.quitMain :
       pass



if __name__ == '__main__':
    main()
