import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name",default="hello")
    args = parser.parse_args()
    print args.name


if __name__=="__main__":
    main()
