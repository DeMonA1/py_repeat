import multiprocessing,time,random


def tim():
    clock = print(time.asctime(time.localtime()))
    return clock

def main():
    for i in range(3):
        p = multiprocessing.Process(target=tim)
        p.start()
        time.sleep(random.random())


if __name__ == "__main__":
    main()
