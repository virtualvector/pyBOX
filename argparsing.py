import sys
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--x",default=2.0,type=float,help="x value")
    args = parser.parse_args()

    print args.x

if __name__ == "__main__":
    main()
