import math

dis1_ = float(input("Введите кратчайшее расстояние между спасателем и кромкой воды, d1 (ярды) => 8: "))
dis2_ = float(input("Введите кратчайшее расстояние от утопающего до берега, d2 (футы) => 10: "))
dis3_ = float(input("Введите боковое смещение между спасателем и утопающим, h (ярды) => 50: "))
v_sand_ = float(input("Введите скорость движения спасателя по песку, v_sand (мили в час) => 5: "))
coefficient_ = float(input("Введите коэффициент замедления спасателя при движении в воде, n => 2: "))
theta1_ = float(input("Введите направление движения спасателя по песку, θ1 (градусы) => 39.413: "))
print("Введённые данные: ")
yard_to_feet = 3
milesPerHour_to_feetPerSecond = 1.466666
pi_ = 3.1415926535897932384626433832795


def calculate_idx(dis1: float(), theta1: float(), coefficient: float(), dis3: float(), dis2: float(), v_sand: float()):
    return float((((((((yard_to_feet * dis1) * (math.tan(((theta1 * pi_) / 180)))) ** 2)
                     + (yard_to_feet * dis1) ** 2)) ** (1 / 2))
                  + (coefficient * (((((dis3 * yard_to_feet) - ((yard_to_feet * dis1)
                                                                * (math.tan(((theta1 * pi_) / 180))))) ** 2)
                                     + (dis2 ** 2)) ** (1 / 2)))) / (v_sand * milesPerHour_to_feetPerSecond))


idx = calculate_idx(dis1_, theta1_, coefficient_, dis3_, dis2_, v_sand_)
print(float(input(f" Кратчайшее расстояние между спасателем и кромкой воды, d1 (ярды) => {dis1_:.0f},\n "
                  f"Направление движения спа5"
                  f"сателя по песку, θ1 (градусы) => {theta1_ :.3f},\n "
                  f"Коэффициент замедления спасателя при движении в воде, n => {coefficient_ :.0f},\n "
                  f"Боковое смещение между спасателем и утопающим, h (ярды) => {dis3_ :.0f},\n "
                  f"Кратчайшее расстояние от утопающего до берега, d2 (футы) => {dis2_ :.0f},\n "
                  f"Скорость движения спасателя по песку, v_sand (мили в час) => {v_sand_ :.0f},\n "
                  f"Решение: \n"
                  f"Если спасатель начнёт движение под углом θ1, равным {theta1_:.0f} градусам, \n"
                  f"он достигнет утопащего через {idx:.1f} секунд")))
