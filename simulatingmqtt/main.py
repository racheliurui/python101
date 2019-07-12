from threading import Thread
import threadfunction
import time
import pub
import vars

def main():
   #https://morvanzhou.github.io/tutorials/python-basic/threading/3-join/
   # About how to join
   t1=Thread(target=threadfunction.refresh_sensor1,args=())
   t2=Thread(target=threadfunction.refresh_sensor2,args=())
   t3=Thread(target=threadfunction.killMain,args=())
   t4=Thread(target=pub.publish_readings,args=())
   t1.daemon=True
   t2.daemon=True
   t3.daemon=True
   t4.daemon=True
   t1.start()
   t2.start()
   t3.start()
   t4.start()
   while not vars.quitMain :
       pass



if __name__ == '__main__':
    main()
