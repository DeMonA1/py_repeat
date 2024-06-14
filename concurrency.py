import os, subprocess


os.getpid()
os.getcwd()



ret = subprocess.getoutput('date /t')
ret
ret = subprocess.check_output(['date ','/t'], shell=True)
ret
ret = subprocess.getstatusoutput('date /t')
ret
ret = subprocess.call(['date','/t'], shell=True)
ret


os.cpu_count()
os.system('date /t')