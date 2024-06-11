import calendar
from datetime import date, timedelta, time, datetime


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