import re
import subprocess

from decimal import Decimal

PINGOUT = '(\d+\.\d+)'
MATCH = 2   # Indexed by 1, not 0

class Ping(object):
    def __init__(self, count):
        self.count = count
        self.patt = re.compile(PINGOUT)

    def time(self, host):
        output = subprocess.Popen(["ping", "-c", str(self.count), host], stdout=subprocess.PIPE)
        
        result = output.stdout.readlines()[-1].strip()
        m = self.patt.findall(result)
        # Change indexing to 0
        avg_time = m[MATCH - 1]

        return Decimal(avg_time)

if __name__ == "__main__":
    p = Ping(5)
    print(p.time("uoit.ca"))
