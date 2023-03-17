import time
import pyautogui as pg
from config import Config
from text_colors import TextColors
from utils.map import Map


class FightActions:
    def __init__(self):
        pass

    def exchange_position(self):
        # Move o cursor ao personagem próximo aos monstros

        map = Map()

        current_map = map.verify_current_map()

        [x, y] = current_map.fight.before_fight_exchange_pos.get_coordinates

        time.sleep(Config.DELAY_IN_SECONDS)
        pg.moveTo(x + 10, y + 10)
        time.sleep(Config.DELAY_IN_SECONDS)
        pg.click()
        time.sleep(Config.DELAY_IN_SECONDS)

        # Troca de posição
        try:
            exchangePos = pg.locateOnScreen(
                '././img/game_structure/echanger.png', confidence=0.8, )
            if exchangePos:
                pg.moveTo(exchangePos[0], exchangePos[1])
                pg.move(50, 20)
                pg.click()
                print(f"{TextColors.OKGREEN}[OK] Changed position.")

        except:
            print(f"{TextColors.WARNING}[WARN] Sadida is already positioned?")

    def press_ready(self):
        readyPos = pg.locateOnScreen(
            '././img/game_structure/ready.png', confidence=0.8, )
        if readyPos:
            pg.moveTo(readyPos[0] + 25, readyPos[1] + 25)
            pg.click()

    def move_to_mobs_in_battle(self):
        map = Map()

        current_map = map.verify_current_map()

        [x, y] = current_map.fight.cell_next_to_mobs.get_coordinates

        pg.moveTo(x, y)
        time.sleep(Config.DELAY_IN_SECONDS * 2)
        pg.click()
        time.sleep(Config.DELAY_IN_SECONDS)

    def use_chosen_spells(self):

        # Usa 2 vezes para caso dê falha crítica.

        # Vento envenenado
        self.use_spell_with_critical_failure_safety('1')

        # Terremoto
        self.use_spell_with_critical_failure_safety('2')

    def use_spell_with_critical_failure_safety(self, shortcut: str):
        for _ in range(2):
            pg.press(shortcut)
            time.sleep(Config.DELAY_IN_SECONDS)
            pg.click()
            time.sleep(Config.DELAY_IN_SECONDS * 1.25)

    def pass_turn(self):
        passPos = pg.locateOnScreen(
            '././img/game_structure/pass.png', confidence=0.8)

        if passPos:
            pg.moveTo(passPos[0], passPos[1])
        time.sleep(Config.DELAY_IN_SECONDS)
        pg.click()

    def verify_finished_fight(self):
        try:
            fight_finished = pg.locateOnScreen(
                '././img/game_structure/close_fight.png', confidence=0.9)

            if fight_finished:
                try:
                    levelUpPos = pg.locateOnScreen(
                        '././img/game_structure/ok_level_up.png', confidence=0.9)
                    if levelUpPos:
                        pg.moveTo(levelUpPos[0] + Config.IMAGE_OFFSET,
                                  levelUpPos[1] + Config.IMAGE_OFFSET)
                    time.sleep(Config.DELAY_IN_SECONDS)
                    pg.click()
                    time.sleep(Config.DELAY_IN_SECONDS)
                    print('Upou de level.')

                except:
                    print('Não upou.')

                pg.moveTo(fight_finished[0] + Config.IMAGE_OFFSET,
                          fight_finished[1] + Config.IMAGE_OFFSET)
                print('Luta terminou.')
                time.sleep(Config.DELAY_IN_SECONDS / 2)
                pg.click()
                time.sleep(Config.DELAY_IN_SECONDS)
                return True
        except:
            'Luta ainda não finalizou.'

    def loop_pass(self):
        fight_finished = None

        pass_pos = pg.locateOnScreen(
            '././img/game_structure/pass.png', confidence=0.8)

        if pass_pos:
            pg.moveTo(pass_pos[0] + 25, pass_pos[1] + 25)

        while not fight_finished:
            try:
                time.sleep(Config.DELAY_IN_SECONDS * 2)
                pg.move(50, 0)
                pg.move(-50, -0)
                time.sleep(1)
                pg.click()
                if self.verify_finished_fight():
                    return True

            except:
                print('Ainda estou passando...')
