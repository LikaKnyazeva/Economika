# Исходные данные
# Не меняются
Vpoch = 2500000
Apoch = 380000
t = 3

#Меняются
# 2
price_build = 87000
# 3
price_car = 18000
# 4
price_comp = 12000
# 5
price_verst = 200000
# 12
tax_build = 11300
# 13
tax_car = 1600
# 14
tax_comp = 500
# 15
tax_verst = 16000
# 16
mont_build = 5200
# 17
mont_car = 200
# 18
mont_comp = 100
# 19
mont_verst = 7000
# 2
t_enter_build = 6
# 3
t_enter_car = 3
# 4
t_enter_comp = 3
# 5
t_enter_verst = 7
# 6
V_vuv_build = 110000
# 7
V_vuv_car = 16000
# 8
V_vuv_comp = 8000
# 9
V_vuv_verst = 191000
# 6
t_exit_build = 3
# 7
t_exit_car = 2
# 8
t_exit_comp = 6
# 9
t_exit_verst = 1
# 10
q_10 = 3560
# 11
q_11 = 1800
# 20
p = 4.49


# Расчеты


def sum(a, b, c):
    result = a + b + c
    return result


def mult(a, b):
    result = a * b
    return result


Vvv_build = sum(price_build, tax_build, mont_build)
Vvv_car = sum(price_car, tax_car, mont_car)
Vvv_comp = sum(price_comp, tax_comp, mont_comp)
Vvv_verst = sum(price_verst, tax_verst, mont_verst)

Vvv_sum = mult(Vvv_build, (t_enter_build / 12)) + mult(Vvv_car, (t_enter_car / 12)) + mult(Vvv_comp,
                                                                                           (t_enter_comp / 12)) + mult(
    Vvv_verst, (t_enter_verst / 12))
Vvuv_sum = mult(V_vuv_build, (t_exit_build / 12)) + mult(V_vuv_car, (t_exit_car / 12)) + mult(V_vuv_comp, (
            t_exit_comp / 12)) + mult(V_vuv_verst, (t_exit_verst / 12))
V_ser = Vpoch + Vvv_sum - Vvuv_sum

Vv_build = Vvv_build / (1 + (p / 100))**3
Vv_car = Vvv_car / (1 + (p / 100))**3
Vv_comp = Vvv_comp / (1 + (p / 100))**3
Vv_verst = Vvv_verst / (1 + (p / 100))**3

# Фондовіддача
F_vid = q_10 * q_11 / V_ser
# Фондомісткість
F_mist = V_ser / q_10 * q_11
# Фондоозброєнність
F_ozbr = V_ser / q_11

# Амортизація
Arich_build = mult(Vvv_build, 0.9) / 20
Arich_car = mult(Vvv_car, 0.9) / 5
Arich_comp = mult(Vvv_comp, 0.9) / 3
Arich_verst = mult(Vvv_verst, 0.9) / 5

Azag = Apoch + Arich_build + Arich_car + Arich_comp + Arich_verst

# вартість всіх основних фондів на кінець року
Vkr = Vpoch + (Vvv_build + Vvv_car + Vvv_comp + Vvv_verst) - Azag - (V_vuv_build + V_vuv_car + V_vuv_comp + Vvv_verst)
Vvv_sum_koef = Vvv_build + Vvv_car + Vvv_comp + Vvv_verst
Vub_sum_koef = V_vuv_build + V_vuv_car + V_vuv_comp + Vvv_verst

# Коефіцієнт оновлення
Konov = Vvv_sum_koef/Vkr

# Коефіцієнт вибуття
Kvub = Vub_sum_koef/Vpoch

# Коефіцієнт фізичного зношення
Kfznosh_build = Arich_build*3/Vvv_build
Kfznosh_car = Arich_car*3/Vvv_car
Kfznosh_comp = Arich_comp*3/Vvv_comp
Kfznosh_verst = Arich_verst*3/Vvv_verst

# Коефіцієнт морального зношування
Kmznosh_build = (Vvv_build - Vv_build)/Vvv_build
Kmznosh_car = (Vvv_car - Vv_car)/Vvv_car
Kmznosh_comp = (Vvv_comp - Vv_comp)/Vvv_comp
Kmznosh_verst = (Vvv_verst - Vv_verst)/Vvv_verst

# Загальний коефіцієнт зношення


# Вывод, что писать
print("1. Розрахувати середньорічну вартість основних фондів поточного року та "
      "відновну вартість введених в поточному році основних фондів після трьох років їх експлуатації.")

print("Первісна (повна) вартість")
print("Вп.буд =", str(price_build), "+", str(tax_build), "+", str(mont_build), "=", str(Vvv_build))
print("Вп.маш =", str(price_car), "+", str(tax_car), "+", str(mont_car), "=", str(Vvv_car))
print("Вп.комп =", str(price_comp), "+", str(tax_comp), "+", str(mont_comp), "=", str(Vvv_comp))
print("Вп.верст =", str(price_verst), "+", str(tax_verst), "+", str(mont_verst), "=", str(Vvv_verst))

print("Середньорічна вартість основних фондів")
print("В.вв.сум =", str(Vvv_build), "*", str(t_enter_build / 12), "+", str(Vvv_car), "*", str(t_enter_car / 12),
      str(Vvv_comp), "*", str(t_enter_comp / 12), str(Vvv_verst), "*", str(t_enter_verst / 12), "=", str(Vvv_sum))
print("В.вив.сум =", str(V_vuv_build), "*", str(t_exit_build / 12), "+", str(V_vuv_car), "*", str(t_exit_car / 12),
      "+", str(V_vuv_comp), "*", str(t_exit_comp / 12), "+", str(V_vuv_verst), "*", str(t_exit_verst / 12), "=",
      str(Vvuv_sum))
print("В.сер =", str(Vpoch), "+", str(Vvv_sum), "-", str(Vvuv_sum), "=", str(V_ser))

print("Відновна вартість")
print("В.в.буд=", str(Vvv_build), "/(1 +", str(p), "/100)) ^ 3) =", str(Vv_build))
print("В.в.маш=", str(Vvv_car), "/(1 +", str(p), "/100)) ^ 3)=", str(Vv_car))
print("В.в.комп=", str(Vvv_comp), "/(1 +", str(p), "/100)) ^ 3)=", str(Vv_comp))
print("В.в.верст=", str(Vvv_verst), "/(1 +", str(p), "/100)) ^ 3)=", str(Vv_verst))

print("2. Розрахувати основні показники використання основних фондів за поточний рік: фондовіддачу, фондомісткість, "
      "фондоозброєність.")

print("Фондовіддача")
print("Фв = ", str(q_10), "*", str(q_11), "/", str(V_ser), "=", str(F_vid))
print("Фондомісткість")
print("Фм = ", str(V_ser), "/", str(q_10), "*", str(q_11), "=", str(F_mist))
print("Фондоозброєність")
print("Фо = ", str(V_ser), "/", str(q_11), "=", str(F_ozbr))

print("3. Визначити коефіцієнти оновлення та вибуття за поточний рік.")

print("Розрахувати амортизацію")
print("А.річ.буд = ", str(Vvv_build), "*0.9)/20 =", str(Arich_build))
print("А.річ.маш = ", str(Vvv_car), "*0.9)/5 =", str(Arich_car))
print("А.річ.комп = ", str(Vvv_comp), "*0.9)/3 =", str(Arich_comp))
print("А.річ.верст = ", str(Vvv_verst), "*0.9)/5 =", str(Arich_verst))
print("А.річ.заг. =", str(Apoch), "+", str(Arich_build), "+", str(Arich_car), "+", str(Arich_comp), "+",
      str(Arich_verst), "=", str(Azag))

print("Вартість всіх основних фондів на кінець року")
print("В.к.р = ", str(Vpoch), "+ (", str(Vvv_build), "+", str(Vvv_car), "+", str(Vvv_comp), "+", str(Vvv_verst), ") - ",
      str(Azag), "-  (", str(V_vuv_build), "+", str(V_vuv_car), "+", str(V_vuv_comp), "+", str(Vvv_verst), ") =",
      str(Vkr))

print("Коефіцієнт оновлення")
print("К.оновл = ", str(Vvv_sum_koef), "/", str(Vkr), "=", str(Konov))

print("Коефіцієнт вибуття")
print("К.виб = ", str(Vub_sum_koef), "/", str(Vpoch), "=", str(Kvub))

print("4. Визначити коефіцієнти фізичного, морального та загального зношення усіх "
      "придбаних в поточному році основних фондів після трьох років їх експлуатації.")

print("Коефіцієнт фізичного зношення")
print("К.ф.знош.буд. = ", str(Arich_build), "*3/", str(Vvv_build), "=", str(Kfznosh_build))
print("К.ф.знош.маш. = ", str(Arich_car), "*3/", str(Vvv_car), "=", str(Kfznosh_car))
print("К.ф.знош.комп. = ", str(Arich_comp), "*3/", str(Vvv_comp), "=", str(Kfznosh_comp))
print("К.ф.знош.верст. = ", str(Arich_verst), "*3/", str(Vvv_verst), "=", str(Kfznosh_verst))

print("Коефіцієнт морального зношування")
print("К.мор.знош.буд. =  (", str(Vvv_build), "-", str(Vv_build), ") /", str(Vvv_build), "=", str(Kmznosh_build))
print("К.мор.знош.маш. =  (", str(Vvv_car), "-", str(Vv_car), ") /", str(Vvv_car), "=", str(Kmznosh_car))
print("К.мор.знош.комп. =  (", str(Vvv_comp), "-", str(Vv_comp), ") /", str(Vvv_comp), "=", str(Kmznosh_comp))
print("К.мор.знош.верст. =  (", str(Vvv_verst), "-", str(Vv_verst), ") /", str(Vvv_verst), "=", str(Kmznosh_verst))


