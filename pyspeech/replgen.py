import pyttsx3


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
    print(r"""  _____   _____ ___ ___ ___ ___ _  _     _    _____   _____
 | _ \ \ / / __| _ \ __| __/ __| || |___| |  |_ _\ \ / / __|
 |  _/\ V /\__ \  _/ _|| _| (__| __ |___| |__ | | \ V /| _|
 |_|   |_| |___/_| |___|___\___|_||_|   |____|___| \_/ |___|
                                                            """)
    print("v0.1.2")
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