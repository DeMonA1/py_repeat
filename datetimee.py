import calendar, time, locale
from datetime import date, timedelta, time, datetime


#datatime, calendar
calendar.isleap(1900)
calendar.isleap(2002)
calendar.isleap(2000)

halloween = date(2019, 10, 31)
halloween
halloween.day
halloween.month
halloween.year
halloween.isoformat()

now = date.today()
one_day = timedelta(days=1)
tomorrow = now + one_day
tomorrow
now + 17*one_day
yesterday = now - one_day
yesterday

noon = time(12,0,0)
noon
noon.hour

some_day = datetime(2019, 1,2,3,4,5,6)
some_day
some_day.isoformat()
now = datetime.now()
now.year
now.microsecond

noon = time(12)
this_day = date.today()
noon_today = datetime.combine(this_day, noon)
noon_today
noon_today.date()
noon_today.time()



#time
now = time.time()
now
time.ctime(now)
nw = time.localtime()
time.gmtime(now)
nw[0]
print(list(nw[x] for x in range(9)))
time.mktime(nw)
now = time.time()
time.ctime(now)
fmt = "It's %A, %B, %d, %Y, local time %I:%M:%S%p"
f = time.localtime()
f
time.strftime(fmt, f)
some_day = date(2019, 7, 4)
some_day.strftime(fmt)  #12.00
some_time = time(10, 35)
some_time.strftime(fmt)     #1.1.1900
fmt = "%Y-%m-%d"
time.strptime('2019-01-29', fmt)


halloween = date(2014, 10, 31)
for lag_country in ['en_us', 'fr_fr', 'de_de', 'es_es', 'is_is',]:
    locale.setlocale(locale.LC_TIME, lag_country)
    halloween.strftime('%A, %B, %d')
names = locale.locale_alias.keys()
good_names = [name for name in names if \
              len(name) == 5 and name[2] == '_']
good_names[:5]
de = [name for name in good_names if name.startswith('de')]

with open('today.txt', 'w') as t:
    fmt = "It's %A, %B, %d, %Y, local time %I:%M:%S%p"
    today = datetime.today()
    t.write(today.strftime(fmt))

with open('today.txt','r') as t:
    today_string = t.readline()
    today_string

bir = date(1998, 7, 13)
bir.strftime("It's %A")
delta = timedelta(days=10000)
new_age = bir + delta
new_age.strftime(fmt)