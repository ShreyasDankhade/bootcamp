import argparse

def main():
    parser = argparse.ArgumentParser(
        prog="shreyas-hello",
        description="Prints a friendly greeting"
    )
    parser.add_argument(
        "-n", "--name",
        metavar="NAME",
        default="world",
        help="Who to say hello to (default: %(default)s)"
    )
    args = parser.parse_args()
    print(f"Hello, {args.name}!")

if __name__ == "__main__":
    main()

