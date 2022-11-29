from math import fsum
from random import randint
from statistics import median, stdev

Z_ten_nums = [randint(0, 100) for i in range(10)]
print(*Z_ten_nums, str(f"- это список из десяти целых чисел;"))
#
print(int(fsum(Z_ten_nums)), str(f"- это сумма чисел списка целых чисел;"))
print(int(fsum(Z_ten_nums) / 10), str(f"- это среднее значение списка;"))
print(median(Z_ten_nums), str(f"- это медиана списка;"))
print(stdev(Z_ten_nums), str(f"- это стандартное отклонение списка"))
#
print(randint(1, 100), str(f"- это случайное целое число в интервале от 1 до 100 включительно"))
