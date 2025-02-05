#import dates

#for i in range(10):
#    print(dates)

import datetime
import random

x = datetime.timedelta(minutes=random.randrange(8000))
hoursago = int( x.seconds / 3600 )
minutesago = round( (x.seconds - hoursago*3600)/60 )
print( f"{x.days} days, {hoursago} hours, and {minutesago} minutes ago" )