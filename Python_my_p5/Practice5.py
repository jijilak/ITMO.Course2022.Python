from random import randint
import time


def name_imput(name):
    print("{:d} игрок. Введите имя: ".format(name))
    return input()


def move(igrok):
    print("Кубик бросает: ", format(igrok))
    time.sleep(3)
    tur_igrok = randint(1, 6)
    print("Выпало: ", tur_igrok)
    return tur_igrok


def steps_game(igrok1, igrok2):
    steps = int(input("Введите количество раундов: "))
    summa_igrok1 = 0
    summa_igrok2 = 0
    for x in range(steps):
        print("Тур №: ", x + 1)
        tur_igrok1 = move(igrok1)
        summa_igrok1 += tur_igrok1
        tur_igrok2 = move(igrok2)
        summa_igrok2 += tur_igrok2
        print(igrok1, "получено очков: ", tur_igrok1, "Сумма очков: ", summa_igrok1)
        print(igrok2, "получено очков: ", tur_igrok2, "Сумма очков: ", summa_igrok2)
    return [summa_igrok1, summa_igrok2]
#


def who_win(igrok1, igrok2, summa_igrok1, summa_igrok2):
    if summa_igrok1 > summa_igrok2:
        print("Выиграл: ", igrok1)
    elif summa_igrok1 < summa_igrok2:
        print("Выиграл: ", igrok2)
    else:
        print("Ничья!")
