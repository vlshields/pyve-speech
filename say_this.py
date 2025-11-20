import argparse
from pyspeech.replgen import repl_mode, say_something, create_engine 


def main():
    parser = argparse.ArgumentParser(
        usage="%(prog)s [-h] [-f] [-s] [-r] [TEXT]",
        description="Text to speech converter"
    )
    parser.add_argument("text", nargs="?", help="Text to speak (not needed in REPL mode)")
    parser.add_argument(
        "-f", "--female", action="store_true", help="Use female voice (default: male)"
    )
    parser.add_argument(
        "-s", "--save", action="store_true", help="save to file (default: false)"
    )
    parser.add_argument(
        "-r", "--repl", action="store_true", help="Run in continuous REPL mode (type 'q' to quit)"
    )
    args = parser.parse_args()

    if args.repl:
        repl_mode(args.female, args.save)
    elif args.text:
        say_something(args.text, args.female, args.save)
    else:
        parser.error("Please provide text to speak or use --repl for interactive mode")


if __name__ == "__main__":
    main()
    
