from time import sleep

from colorama import Fore


class TrLight:
    _states = {Fore.RED + 'КРАСНЫЙ': 7, Fore.YELLOW + 'ЖЁЛТЫЙ': 2, Fore.GREEN + 'ЗЕЛЁНЫЙ': 5}
    __color = ''

    def running(self):
        while True:
            for color, sw_time in self._states.items():
                self.__color = color
                print(self.__color)
                sleep(sw_time)


tl = TrLight()
tl.running()
