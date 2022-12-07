from datetime import datetime

datetime1 = datetime.now()

year = datetime1.year
month = datetime1.month
day = datetime1.day
hour = datetime1.hour
minutes = datetime1.minute
seconds = datetime1.second
microseconds = datetime1.microsecond

print('Today\'s datetime is: ', str(hour) + ':' + str(minutes) + ':' + str(seconds) + ':' + str(microseconds)
      + ' ' + str(day) + '/' + str(month) + '/' + str(year))

utc0 = datetime.utcfromtimestamp(0)  # 1970-01-01 00:00:00
datetime2 = '2022-09-23 13:00'
datetime2 = datetime.strptime(datetime2, '%Y-%m-%d %H:%M')  # 2022-09-23 13:00

print(int(abs(utc0 - datetime2).total_seconds()))
