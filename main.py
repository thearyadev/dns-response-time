import json
import time
import requests
import socket
from timeit import default_timer as timer

# test_domains
domain = "dnstest.avery.local"
previous = list()


def get_time(addr):
    try:
        s = timer()
        address = socket.gethostbyname(addr)
        e = timer()
        return float(f"{(e - s) * 1000:.2f}")
    except:
        return "error"


while True:
    rtime = get_time(domain)
    print(rtime)
    if rtime == "error":
        requests.post("http://10.0.0.192/api/webhook/dns-response",
                      json={"message": "DNS Server(s) did not respond"})
    else:
        previous.append(rtime)
        remove_err = [i for i in previous if not isinstance(i, str)]
        average = sum(remove_err) / len(remove_err)

        if (rtime / average) > 5.0:
            requests.post("http://10.0.0.192/api/webhook/dns-response",
                          json={"message": f"Slow DNS response. t={rtime}; d={rtime / average}"})
        if len(previous) > 10:
            previous.pop(0)
    time.sleep(10)
