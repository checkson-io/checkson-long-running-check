import sys
import os
from time import sleep

DELAY = os.getenv('DELAY', default="90")

print(f"Waiting {DELAY} seconds before exiting...")
sleep(int(DELAY))
print("Exiting...")
sys.exit(0)
