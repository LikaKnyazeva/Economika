# Исходные данные

Vpoch = 25000000
price_build = 87000
price_car = 18000
price_comp = 12000
price_verst = 200000
tax_build = 11300
tax_car = 1600
tax_comp = 500
tax_verst = 16000
mont_build = 5200
mont_car = 200
mont_comp = 100
mont_verst = 7000
t_enter_build = 6
t_enter_car = 3
t_enter_comp = 3
t_enter_verst = 7
V_vuv_build = 110000
V_vuv_car = 16000
V_vuv_comp = 8000
V_vuv_verst = 191000
t_exit_build = 3
t_exit_car = 2
t_exit_comp = 6
t_exit_verst = 1
q_10 = 3560
q_11 = 1800
t = 3
p = 4.49

# Расчеты


def sum(a, b, c):
    result = a + b + c
    return result


def mult(a, b):
    result = a*b
    return result


Vvv_build = sum(price_build, tax_build, mont_build)
Vvv_car = sum(price_car, tax_car, mont_car)
Vvv_comp = sum(price_comp, tax_comp, mont_comp)
Vvv_verst = sum(price_verst, tax_verst, mont_verst)

Vvv_sum = mult(Vvv_build, (t_enter_build/12))+ mult(Vvv_car, (t_enter_car/12))+mult(Vvv_comp, (t_enter_comp/12))+mult(Vvv_verst, (t_enter_verst/12))
Vvuv_sum = mult(V_vuv_build, (t_exit_build/12)) + mult(V_vuv_car, (t_exit_car/12)) + mult(V_vuv_comp, (t_exit_comp/12)) + mult(V_vuv_verst, (t_exit_verst/12))
V_ser = Vpoch + Vvv_sum - Vvuv_sum

Vv_build = Vvv_build/(int(1 + (p/100)) ^ 3)
Vv_car = Vvv_car/(int(1 + (p/100)) ^ 3)
Vv_comp = Vvv_comp/(int(1 + (p/100)) ^ 3)
Vv_verst = Vvv_verst/(int(1 + (p/100)) ^ 3)

# Фондовіддача
F_vid = q_10*q_11/V_ser
# Фондомісткість
F_mist = V_ser/q_10*q_11
# Фондоозброєнність
F_ozbr = V_ser/q_11

# Вывод, что писать
print("1. Розрахувати середньорічну вартість основних фондів поточного року та "
      "відновну вартість введених в поточному році основних фондів після трьох років їх експлуатації.")

print("Первісна (повна) вартість")
print("Вп.буд =", str(price_build), "+", str(tax_build), "+", str(mont_build), "=", str(Vvv_build))
print("Вп.маш =", str(price_car), "+", str(tax_car), "+", str(mont_car), "=", str(Vvv_car))
print("Вп.комп =", str(price_comp), "+", str(tax_comp), "+", str(mont_comp), "=", str(Vvv_comp))
print("Вп.верст =", str(price_verst), "+", str(tax_verst), "+", str(mont_verst), "=", str(Vvv_verst))

print("Середньорічна вартість основних фондів")
print("В.вв.сум =", str(Vvv_build), "*", str(t_enter_build/12), "+", str(Vvv_car), "*", str(t_enter_car/12),
      str(Vvv_comp), "*", str(t_enter_comp/12), str(Vvv_verst), "*", str(t_enter_verst/12), "=", str(Vvv_sum))
print("В.вив.сум =", str(V_vuv_build), "*", str(t_exit_build/12), "+", str(V_vuv_car), "*", str(t_exit_car/12),
      "+", str(V_vuv_comp), "*", str(t_exit_comp/12), "+", str(V_vuv_verst), "*", str(t_exit_verst/12), "=",
      str(Vvuv_sum))
print("В.сер =", str(Vpoch), "+", str(Vvv_sum), "-", str(Vvuv_sum), "=", str(V_ser))

print("Відновна вартість")
print("В.в.буд=",  str(Vvv_build), "/(1 +", str(p), "/100)) ^ 3) =", str(Vv_build))
print("В.в.маш=",  str(Vvv_car), "/(1 +", str(p), "/100)) ^ 3)=", str(Vv_car))
print("В.в.комп=",  str(Vvv_comp), "/(1 +", str(p), "/100)) ^ 3)=", str(Vv_comp))
print("В.в.верст=",  str(Vvv_verst), "/(1 +", str(p), "/100)) ^ 3)=", str(Vv_verst))

print("2. Розрахувати основні показники використання основних фондів за поточний рік: фондовіддачу, фондомісткість, "
      "фондоозброєність.")

print("Фондовіддача")
print("Фв = ", str(q_10), "*", str(q_11), "/", str(V_ser), "=", str(F_vid))
print("Фондомісткість")
print("Фм = ", str(V_ser), "/", str(q_10), "*", str(q_11), "=", str(F_mist))
print("Фондоозброєність")
print("Фо = ", str(V_ser), "/", str(q_11), "=", str(F_ozbr))


print("3. Визначити коефіцієнти оновлення та вибуття за поточний рік.")
print("")



