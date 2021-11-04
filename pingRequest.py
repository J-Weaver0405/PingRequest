from pprint import pprint
# from numpy import numpy as np

def parse_ping_request(out_file="ping_out.txt"):
    final_res = {}
    with open(out_file, 'r') as stuff:
        tmp = []
        lines = stuff.readlines()
        for row in lines:
            pprint(row)
            if row.startswith('PING'):
                continue 
            elif row.startswith('---'):
                final_row_parts = row.split()

                final_res[final_row_parts[1]] = tmp
                tmp = []
            else:
                tmp.append(row.split())
    return final_res


class PingGroup():
    def __init__(self, pings = {}):
        self._pings = pings

    @property 
    def pings(self):
        return self._pings  

    @pings.setter 
    def pings(self, pings):
        self._pings = pings
        
    def add_ping(self, ping):
        if ping.ip not in self._pings:
            self._pings[ping.ip] = [ping]
        else:
            self._pings[ping.ip].append(ping)
    
    def min_ping(self, ip='142.250.80.78:'):
        return min([entry.time for entry in self._pings[ip]])
    
    def max_ping(self):
        max_ping = max(self._pings)
    
    def avg_ping(self, domain, n = 3):
        if domain in self._pings:
            all_reqs = [entry.time for entry in self._pings[domain]]
            summ = sum(all_reqs)
            return round(summ/len(all_reqs), n)
        else:
            raise ValueError(f"No domain{domain}")

        
class PingRequest():
    def __init__(self, ip_address, URL, amt_bytes, time):
        self._ip = ip_address
        self._URL = URL
        self._amt_bytes = amt_bytes
        self._time = time


    def __str__(self):
        return f" URL: {self._URL}; time:{self._time} amt of bytes: {self.amt_bytes} ip address: {self._ip}"
    

    @property
    def ip(self):
        return self._ip


    @ip.setter
    def ip(self, ip):
        if ip_address < 0:
            raise ValueError("Not a Valid Address")
        self._ip = ip

    @property
    def url(self):
        return self._URL


    @url.setter
    def url(self,url):
        if url.endswith(".com") or url.endswith(".net"):
            raise ValueError("not a Valid Address")
        self._URL = URL


    @property
    def amt_bytes(self):
        return self._amt_bytes


    @amt_bytes.setter
    def amt_bytes(self, amt_bytes):
        if amt_bytes < 0:
            raise ValueError("Amount has to be greater than 0. ")
        self._amt_bytes = amt_bytes

    
    @property
    def time(self):
        return self._time
        
    @time.setter
    def time(self, time):
        self._time = time
        


if __name__ == '__main__':
	#for parsing file
	#for row in parse_ping_request():
		#parse from file into pingRequest 
		# add to PingGroup

	# sample of how to add to ping group
    # ip_address, URL, amt_bytes, time
    # pr1 = PingRequest("0.0.0.0","google.com",64, 19.062)
    # pr2 = PingRequest("0.0.0.0","google.com",64, 20.833)
    # pg.add_ping(pr1)
    # pg.add_ping(pr2)
    
    # for ping in pg.pings:
    #     print(ping) 

    # key is domain name, values are the requests/ info associated with domain
    data = parse_ping_request()
    pg = PingGroup()
    for key,vals in data.items():
        vals = vals[2:-1]
        pprint(vals)
        for val in vals:
        #ip_address, URL, amt_bytes, time
            if len(val) > 0:
                if "=" in val[-2]:
                    _, ms = val[-2].split("=")
                    pr = PingRequest(val[3], key,
    key,val[0],float(ms))
                    pg.add_ping(pr)
    pprint(pg.min_ping(""))
    pprint(pg.calc_avg_ms("facebook.com"))