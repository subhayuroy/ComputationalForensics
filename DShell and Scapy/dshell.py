import scapy, GeoIP
from scapy import *

geoIp = GeoIP.new(GeoIP.GEOIP_MEMORY_CACHE)  #locates the Geo IP address

def locatePackage(pkg):
    src = pkg.getlayer(IP).src
    dst = pkg.getlayer(IP).dst #gets destination IP address

    srcCountry = geoIp.country_code_by_addr(src) #gets Country details of source

    dstCountry = geoIp.country_code_by_addr(dst) #gets country details of destination

    print(src+"("+srcCountry+") >> "+dst+"("+dstCountry+")\n")