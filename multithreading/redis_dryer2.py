import redis, os, time, multiprocessing


def dryer():
    conn = redis.Redis()
    pid = os.getpid()
    timeout = 20
    print("Dryer process %s is starting" % pid)
    while True:
        msg = conn.blpop('dishes', timeout)
        if not msg:
            break
        val = msg[1].decode('utf-8')
        if val == 'quit':
            break
        print('%s: dried %s' % (pid, val))
        time.sleep(0.1)
    print('Dryer process %s is done' % pid)

    
if __name__ == '__main__':
    DRYERS = 3
    for num in range(DRYERS):
        p = multiprocessing.Process(target=dryer)
        p.start()