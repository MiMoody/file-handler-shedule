import time
import random
import os

while True:
    time.sleep(0.1)
    with open(r"./file.txt", "a") as f:
        rand = random.randint(0,100000)
        f.write("\n")
        f.write(f"Number-{rand}:pid-{os.getpid()}")