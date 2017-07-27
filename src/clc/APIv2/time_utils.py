"""
Time utility functions.

"""


import time
import calendar
from datetime import datetime


def ZuluTSToSeconds(ts):
	return(calendar.timegm(datetime.strptime(ts,"%Y-%m-%dT%H:%M:%SZ").utctimetuple()))


def SecondsToZuluTS(secs=None):
	"""Returns Zulu TS from unix time seconds.

	If secs is not provided will convert the current time.
	"""

	if not secs:  secs = int(time.time())

	return(datetime.utcfromtimestamp(secs).strftime("%Y-%m-%dT%H:%M:%SZ"))



if __name__ == "__main__":
	now = int(time.time())

	print "Now:     %s" % now
	print "To TS:   %s" % SecondsToZuluTS(now)
	print "To Secs: %s" % ZuluTSToSeconds(SecondsToZuluTS(now))

