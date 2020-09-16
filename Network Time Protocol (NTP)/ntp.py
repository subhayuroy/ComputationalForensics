import ntplib
import time

NIST = 'nist1-macon.macon.ga.us'
ntp = ntplib.NTPClient()
ntpResponse = ntp.request(NIST)

if (ntpResponse):
   now = time.time()
   diff = now-ntpResponse.tx_time
   print(diff)