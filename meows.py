import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n")
args = parser.parse_args() #parse_args will look at sys automatically

for _ in range(int(args.n)):
    print("meow")