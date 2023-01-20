from argparse import ArgumentParser
from time import sleep
import subprocess

parser = ArgumentParser()
parser.add_argument('time', type=int)
args = parser.parse_args()
print(f'starting timer of {args.time} seconds')
for _ in range(args.time):
    print('.', end='', flush=True)
    sleep(1)
print('DONE!')

subprocess.run(["python", "timer.py", "5"])