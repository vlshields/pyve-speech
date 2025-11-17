import pyttsx3
import argparse


def say_some_wisdom(quotation: str, female: bool = False) -> None:
    engine = pyttsx3.init()
    engine.setProperty("rate", 125)
    engine.setProperty("volume", 1.0)

    voices = engine.getProperty("voices")
    # 0 for male, 1 for female (typically)
    voice_index = 1 if female else 0
    engine.setProperty("voice", voices[voice_index].id)

    engine.say(quotation)
    engine.runAndWait()

    engine.save_to_file(quotation, "output.wav")
    engine.runAndWait()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Text to speech converter")
    parser.add_argument("text", help="Text to speak")
    parser.add_argument(
        "-f", "--female", action="store_true", help="Use female voice (default: male)"
    )
    args = parser.parse_args()

    say_some_wisdom(args.text, args.female)
