import gevent, socket
from gevent import monkey; monkey.patch_all()


hosts =  ['www.crappytaxidermy.com', 'www.walterpottertaxidermy.com',
 'www.antique-taxidermy.com']
jobs = [gevent.spawn(socket.gethostbyname, host) for host in hosts]
gevent.joinall(jobs, timeout=5)
for job in jobs:
    print(job.value)