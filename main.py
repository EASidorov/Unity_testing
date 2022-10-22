import unittest
import time

from altunityrunner import *


class SecurityRoom():
    def __init__(self, altdriver):
        self.altdriver = altdriver

    def load(self):
        return self.altdriver.load_scene('SecurityRoom')

    @property
    def guard(self):
        return self.altdriver.wait_for_object(By.NAME, 'Guard')

    @property
    def VO(self):
        return self.altdriver.find_object(By.NAME, 'VO')


class Market():
    def __init__(self, altdriver):
        self.altdriver = altdriver

    def load(self):
        return self.altdriver.load_scene('Market')


class MyFirstTest(unittest.TestCase):
    altdriver = None

    @classmethod
    def setUpClass(cls):
        cls.altdriver = AltUnityDriver()

    @classmethod
    def tearDownClass(cls):
        cls.altdriver.stop()

    """Тест: Подойти к охраннику. Подтверждение: Проиграный звук"""
    # def test_move_to_guard(self):
    #     Secrom = SecurityRoom(self.altdriver)
    #     Secrom.load()
    #     self.altdriver.click(Secrom.guard.get_screen_position())
    #     time.sleep(5)
    #     if Secrom.VO.get_component_property("UnityEngine.AudioSource", "clip", 'UnityEngine.AudioModule'):
    #         return True


    """Тест: Перейти в локацию Рынок и поднять монету. Подтверждение: появление изображения в слоте инвентаря"""
    # def test_coin_pick_up(self):
    #     self.altdriver.find_object(By.NAME, 'DoorToMarketInteractable').click()
    #     time.sleep(5)
    #     self.altdriver.find_object(By.NAME, 'CoinInteractable').click()
    #     time.sleep(5)
    #     inv1 = self.altdriver.find_object(By.NAME, 'ItemSlot0/ItemImage')
    #     if inv1.get_component_property('UnityEngine.UI.Image', 'sprite', 'UnityEngine.UI'):
    #         return True

    """Тест: Перейти обратно в локацию Команата охраны. Подтверждение: возвращение текущей сцены"""
    # def test_go_to_security_room(self):
    #     Market(self.altdriver).load()
    #     self.altdriver.find_object(By.NAME, 'DoorToSecurityRoom').click()
    #     if self.altdriver.get_current_scene() == 'SecurityRoom':
    #         return True


