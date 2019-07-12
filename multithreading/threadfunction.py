import time
import vars



#https://www.geeksforgeeks.org/python-different-ways-to-kill-a-thread/
# By starting the thread as demon, we don't worry about how to stop thread; just stop it with the main
def threadfunction1():
    while True:
      print("threadfunction1" )  
      vars.balance=vars.balance+1
      print("threadfunction1, balance updated as " + str(vars.balance)  )  
      time.sleep(1)



def threadfunction2():
    while True:
      print("threadfunction2" )      
      vars.balance=vars.balance+1
      print("threadfunction2, balance updated as " + str(vars.balance)  )  
      time.sleep(2)
  

def killMain():    
    while True:
       i = input("Enter text (or Enter to quit): ")
       if not i:
          break
    print("Your input:", i)
    vars.quitMain=True
    print("While loop has exited")  