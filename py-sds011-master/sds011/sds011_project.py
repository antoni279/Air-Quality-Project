#import sds011
from sds011 import *
import time
import datetime
sensor = SDS011("/dev/ttyUSB0")

# Turn-on sensor 
# sensor.sleep(sleep=False)

# Turn-off sensor
# sensor.sleep(sleep=True)

# Getting Data
# pmt_2_5, pmt_10 = sensor.query()

sensor.sleep(sleep=False)
time.sleep(10)
pmt_2_5, pmt_10 = sensor.query()
print (datetime.datetime.now(), end='')
print(f"   PMT2.5: {pmt_2_5} μg/m3 ", end='')
print(f"   PMT10: {pmt_10} μg/m3")
sensor.sleep(sleep=True)
time.sleep(2)


