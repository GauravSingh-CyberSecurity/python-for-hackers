# https://docs.python.org/3/library/threading.html

'''
Threads are the smallest unit of execution within a process in a computer program. They allow the program to perform multiple
tasks concurrently, making it appear as if multiple parts of the program are running simultaneously. Each thread has its 
own set of instructions,stack, and register state, but they share the same memory space and resources of the process. This allows
threads to communicatewith each other more efficiently than separate processes, which have their own memory space and resources.
threading in python is basically a way to tell your code to do more than one
thing at once.

with python each process has at least one thread that is called main thread
'''


import threading,time
from datetime import datetime

def sleeper(i):
    print("hello from %d!"%i)
    time.sleep(i)
    print("goodbye from %d!"%i)



print(datetime.now().strftime("%H:%M:%S"))


'''
# all these functions run sequentially so it takes 0+2+3 sec to execute them all.
sleeper(0)
sleeper(2)
sleeper(3)

by using threading we dont have to wait like in above case where we go to
sleep for every time sleeper is called i.e its running sequentially whereas 
the threads run concurrent
'''



'''
# all these threads run concurrently so it takes 5 sec to execute them all.
#threading.Thread(target=sleeper,args=(0,)).start()
#threading.Thread(target=sleeper,args=(1,)).start()
#threading.Thread(target=sleeper,args=(2,)).start()
#threading.Thread(target=sleeper,args=(3,)).start()
#threading.Thread(target=sleeper,args=(4,)).start()
#threading.Thread(target=sleeper,args=(5,)).start()    #highest time is 5 therefore 5 sec to execute

threading.Timer(0,sleeper,[0]).start()
threading.Timer(1,sleeper,[1]).start()
threading.Timer(2,sleeper,[2]).start()
threading.Timer(3,sleeper,[3]).start()

'''


print(datetime.now().strftime("%H:%M:%S"))

#how can we print something on screen & at same time get i/p from user
#print("hello")
#input()
#print("world")   
#i.e we are solving this above code issue where while printing we cant take i/p from user and vice versa




'''
stop = False

def input_thread():
    global stop
    while True:
        user_input = input("Should we stop? ")
        print(">> User says:", user_input)
        if user_input.lower() == "yes" or user_input.lower() == "y":
            stop = True
            break

def output_thread():
    global stop
    count = 0
    while not stop:
        print(count)
        count += 1 
        time.sleep(1)

t1 = threading.Thread(target=input_thread).start()
t2 = threading.Thread(target=output_thread).start()

'''





'''
LOCK : prevents simultaneous access or modification of a resource that are access by multiple threads running concurrently
now lets see locks in threads it helps thread to lock the resource 
before using it so no other thread can access that particular resource at
the same time.

our problem statment here is 
using multiple threads to pop values from a list(resource) i.e all threads access the same resource at 
same time and we will implement locks so that only one thread can access the resource at a time'''

data_lock = threading.Lock()    # this is the lock 
data = [x for x in range(1000)] #(this is the list("resource" that threads want to access and we are going to lock every time a thread is using it))



'''
#lets first impliment this without using the lock and see how these threads work without lock(i.e poping happens in random/unsequintial order bcoz all threads deleting at same time)

def consume_thread():
    global data
    while len(data) > 0:
        print(threading.current_thread().name,data.pop( ))

threading.Thread(target=consume_thread).start() #thread1
threading.Thread(target=consume_thread).start() #thread2
threading.Thread(target=consume_thread).start() #thread3
#i.e not using lock like we did in this case, we are open to encountering the race condition 

'''

#implementing the lock on the list(resource) that is accessed by these threads (i.e popping happens in sequintial order)
def sync_consume_thread():
    global data_lock, data
    while True:
        data_lock.acquire()
        if len(data) > 0:
            print(threading.current_thread().name,data.pop())
        data_lock.release()

threading.Thread(target=sync_consume_thread).start() #thread1
threading.Thread(target=sync_consume_thread).start() #thread2
threading.Thread(target=sync_consume_thread).start() #thread3


#NOTE: when the parent thread exits/finishes/stops it attempts to kill all its child thread. unless the child thread is specified as a daemon.
'''A daemon thread in Python is a thread that runs in the background and does not prevent the program from exiting. This means that if all non-daemon threads have 
finished executing, the Python interpreter can exit even if daemon threads are still running.
Daemon threads are useful for tasks that should not prevent the program from exiting, such as background tasks like monitoring or cleanup operations. You can set a t
hread as a daemon by calling the setDaemon(True) method on the Thread object before starting it.


we can use threading while performing attacks like bruteforcing where we run multiple threads using different password dictionaries  to speed up our attack and increase 
the chances of finding the password, similarly we can use it in many other attacks and defence techniques'''