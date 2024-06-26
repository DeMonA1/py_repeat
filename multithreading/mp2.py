import os, time, multiprocessing

def whoami(name):
    print("I'm %s, in process %s" % (name, os.getpid()))

def loopy(name):
    whoami(name)
    start = 1
    stop = 100000
    for num in range(start, stop):
        print("\tNumber %s of %s. Honk!" % (num, stop))
        time.sleep(1)

if __name__ == '__main__':
    whoami('main')
    p = multiprocessing.Process(target=loopy, args=('loopy',))
    p.start()
    time.sleep(5)
    p.terminate()