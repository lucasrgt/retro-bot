import pyautogui


class GameChecker:
    def verify_if_is_fighting(self) -> bool:
        is_fighting = pyautogui.locateOnScreen(
            '././img/game_structure/ready.png')

        if is_fighting:
            print('[OK] Player is fighting!')
            return True

        else:
            print('[WARN] Player is not fighting! Verifying again.')
            return False
