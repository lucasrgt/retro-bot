from bot import Bot
from utils.detect_window import DetectWindow


def main():
    window = DetectWindow()
    window.detect_window()
    bot = Bot()

    while True:
        bot.state.run()


main()
