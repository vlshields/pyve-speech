import pyttsx3
import argparse


def create_engine(female: bool = False) -> pyttsx3.Engine:
    """Create and configure a pyttsx3 engine instance."""
    engine = pyttsx3.init()
    engine.setProperty("rate", 125)
    engine.setProperty("volume", 1.0)

    voices = engine.getProperty("voices")
    # 0 for male, 1 for female (typically)
    voice_index = 3 if female else 0
    engine.setProperty("voice", voices[voice_index].id)

    return engine


def say_something(quotation: str, female: bool = False, save: bool = False, engine: pyttsx3.Engine = None) -> None:
    """Speak the given text using the provided or a new engine instance."""
    if engine is None:
        engine = create_engine(female)

    engine.say(quotation)

    if save:
        engine.save_to_file(quotation, "output.wav")
    engine.runAndWait()


def repl_mode(female: bool = False, save: bool = False) -> None:
    """Continuous REPL mode for text-to-speech. Type 'q' to quit."""
    print("Text-to-Speech REPL Mode")
    print("Type your text and press Enter to speak it.")
    print("Type 'q' to quit.\n")

    # Create engine once and reuse it
    engine = create_engine(female)

    while True:
        try:
            text = input("> ")
            if text.lower() == 'q':
                print("Goodbye!")
                break
            if text.strip():  # Only speak if there's actual text
                say_something(text, female, save, engine)
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break


if __name__ == "__main__":
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
