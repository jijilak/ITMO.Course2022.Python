from random import randint
import time
# Ввод имен играющих
igrok1 = input("Введите имя 1-го играющего ")
igrok2 = input("Введите имя 2-го играющего ")
summa_igrok1 = 0
tur_igrok1 = 0
summa_igrok2 = 0
tur_igrok2 = 0
for i in range(3):
    # Моделирование бросания кубика первым играющим
    print("Кубик бросает", igrok1)
    time.sleep(2)
    n1 = randint(1, 6)
    print("Выпало:", n1)
    tur_igrok1 = n1
    summa_igrok1 += n1
    # Моделирование бросания кубика вторым играющим
    print("Кубик бросает", igrok2)
    time.sleep(2)
    n2 = randint(1, 6)
    print("Выпало:", n2)
    tur_igrok2 = n2
    summa_igrok2 += n2
    # Определение результата (3 возможных варианта)
    time.sleep(2)
    print("Баллы за тур 1 игрока: ", tur_igrok1)
    print("Баллы за тур 2 игрока: ", tur_igrok2)
    if tur_igrok1 > tur_igrok2:
        print("Выиграл", igrok1)
    elif tur_igrok1 < tur_igrok2:
        print("Выиграл", igrok2)
    else:
        print("Ничья")
time.sleep(4)
print("Сумма баллов за ", i + 1, " тура: ", summa_igrok1)
print("Сумма баллов за ", i + 1, " тура: ", summa_igrok2)
if summa_igrok1 > summa_igrok2:
    print("Выиграл", igrok1)
elif summa_igrok1 < summa_igrok2:
    print("Выиграл", igrok2)
else:
    print("Ничья")
