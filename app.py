import sys
import os
from time import sleep

DELAY = os.getenv('DELAY', default="90")

sleep(int(DELAY))

sys.exit(0)
