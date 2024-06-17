from invoke import task
import time

@task
def mytime(ctx):
    import time
    now = time.time()
    time_str = time.asctime(time.localtime(now))
    print('Local time is', time_str)
