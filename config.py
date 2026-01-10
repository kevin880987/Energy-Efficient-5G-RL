import os

DEBUG = 1 # bool(int(os.environ.get('DEBUG', 1)))
TRAIN = 1 # bool(int(os.environ.get('TRAIN', 0)))
EVAL = 1 # bool(int(os.environ.get('EVAL', 1)))

print("DEBUG:", DEBUG)
print("TRAIN:", TRAIN)
print("EVAL:", EVAL)
print()
