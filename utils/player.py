import pyautogui
import time
from modules.screen.coordinates import Coordinates

from config import Config


class Player:
    def attack_mob(self, pos: Coordinates):
        x, y = pos.get_coordinates

        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(5)

    def eatBread(self):
        try:
            pyautogui.moveTo(1253, 936)
            pyautogui.sleep(Config.DELAY_IN_SECONDS / 2)
            pyautogui.doubleClick()
            print('Comeu o pão.')

        except:
            print('Não conseguiu comer o pão.')
