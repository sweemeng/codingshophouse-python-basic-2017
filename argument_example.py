from argparse import ArgumentParser

def main():
    parser = ArgumentParser(description="My Script")
    parser.add_argument("number", nargs="+", type=int, help="just a numer")
    parser.add_argument("--string", dest="argument_string", type=str, help="just a string")
    
    args=parser.parse_args()
    print(args.number)
    print(args.argument_string)

if __name__ == "__main__":
    main()
