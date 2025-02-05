#dates = ["2 days ago", "3 days ago", "5 hours ago", "2 hours ago", "12 days ago", "8 hours ago", "55 minutes ago"] 

import datetime
import random

x = datetime.timedelta(minutes=random.randrange(8000))
hoursago = int( x.seconds / 3600 )
minutesago = round( (x.seconds - hoursago*3600)/60 )
print( f"{x.days} days, {hoursago} hours, and {minutesago} minutes ago" )