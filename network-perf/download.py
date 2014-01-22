import os
import requests
import time

from decimal import Decimal

class Download(object):
    def __init__(self):
        # Don't care about what's downloaded
        self.path = open(os.devnull, "w")

    def time(self, url):
        start_time = time.time()
        r = requests.get(url, stream=True)

        # Chunk size of 65536 bytes (64 KB)
        for chunk in r.iter_content(chunk_size=(2 ** 16)):
            # Timeout after one hour
            if time.time() - start_time >= 30 * 60:
                return 0

            if chunk:
                self.path.write(chunk)
                self.path.flush()

        return Decimal((time.time() - start_time) * 1000)

if __name__ == "__main__":
    d = Download()
    print(d.time("http://docs.python.org/2/library/time.html"))
