import argparse
from rich.console import Console
from rich.theme import Theme

theme = Theme({"greeting": "bold magenta", "name": "bold green"})
console = Console(theme=theme)

def main():
    parser = argparse.ArgumentParser(
        prog="shreyas-hello",
        description="Prints a friendly, rich-formatted greeting"
    )
    parser.add_argument(
        "-n", "--name",
        metavar="NAME",
        default="world",
        help="Who to say hello to (default: %(default)s)"
    )
    args = parser.parse_args()
    console.print("Hello,", style="greeting", end=" ")
    console.print(args.name + "!", style="name")

if __name__ == "__main__":
    main()
