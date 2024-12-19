# Task "За честь и отвагу!"

import threading
from threading import Thread
import time


class Knight(Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        count_days = 1
        enemy = 100
        print(f'{self.name}, на нас напали!')
        while enemy > 0:
            time.sleep(1)
            enemy = enemy - self.power
            if count_days == 1:
                y = 'день'
            elif count_days == 2:
                y = 'дня'
            else:
                y = 'дней'
            print(f'{self.name} сражается {count_days} {y} осталось {enemy} воинов')
            count_days += 1
            if enemy == 0:
                print(f'{self.name} одержал победу спустя {count_days-1} {y}!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()