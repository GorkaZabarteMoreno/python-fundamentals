from datetime import time

time1 = time()

hour = time1.hour
minutes = time1.minute
seconds = time1.second
microseconds = time1.microsecond

print('Today\'s datetime is: ', str(hour) + ':' + str(minutes) + ':' + str(seconds) + ':' + str(microseconds))
