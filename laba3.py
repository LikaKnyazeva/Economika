# Данные которые не меняются
# Данные которые меняются
# 3
CHvsixv = 1456
# 4
Delta = 45.6
# 6
DeltaT = 56390
# 9
Fd = 1940
# 7
Fn = 256
# 5
CHp = 1649
# 10
DeltaKn = 10
# 1
Vzv = 48000
# 2
Vpl = 59310
# 11
CHzvzag = 239
# 13
CHzv = 220

# Решение

Kn = 1 + (DeltaKn / 100)  # 1
DeltaNop = DeltaT / (Fd * Kn)  # 2
CHozvrr = CHvsixv * (Delta / 100)  # 3
CHoplrr = CHozvrr - DeltaNop  # 4

Kcp = Fn / Fd  # 5
CHyavpl = CHoplrr / Kcp  # 6

CHdoplp = CHvsixv - CHozvrr  # 7
CHvsixl = CHoplrr + CHdoplp  # 8

CHk = 2 * CHvsixl - CHp  # 9
DeltaCHnaim = (CHk - CHp) * (-1)  # 10

PPozvr = Vzv / CHozvrr
PPvsix = Vzv / CHvsixv
PPoplr = Vpl / CHoplrr
PPvsixl = Vpl / CHvsixl

DeltaVchis = PPvsix * (CHvsixl - CHvsixv)*(-1)
DeltaVpp = CHvsixl * (PPvsixl - PPvsix)
DeltaVppch = DeltaVchis + DeltaVpp

CHopprz = Vpl / PPozvr
Eoppr = CHopprz - CHoplrr
Edoppp = (CHozvrr * Vpl / Vzv) - CHozvrr

Kop = CHp / CHvsixv
Koz = CHzvzag / CHvsixv
Kpl = CHzv / CHvsixv

# Ввод на экран

print("1. Розрахувати середньоспискову і явочну чисельність всіх робітників разом, а також окремо основних і допоміжних"
      " робітників у звітному і плановому роках (середньоспискова чисельність допоміжних робітників у плановому році не"
      " змінилась).")
print("Kн = 1 + (", str(DeltaKn), " / 100) =", str(Kn))
print("DeltaNo.p = ", str(DeltaT), "/", str(Fd), " * ", str(Kn), "=", str(DeltaNop))
print("Ч оз.вр.р = ", str(CHvsixv), " * ", str(Delta), "/ 100", "=", str(CHozvrr))
print("Ч оп.лр.р = ", str(CHozvrr), "-", str(DeltaNop), "=", str(CHoplrr))
print("K cп = ", str(Fn), "/ ", str(Fd), "=", str(Kcp))
print("Ч яв.пл.о.р.р = ", str(CHoplrr), "/", str(Kcp), "=", str(CHyavpl))
print("Ч доплп.р = ", str(CHvsixv), "-", str(CHozvrr), "=", str(CHdoplp))
print("Ч всіхлп.р = ", str(CHoplrr), "+", str(CHdoplp), "=", str(CHvsixl))
print("")
print("")
print("2. Розрахувати чисельність додаткового найму (чи звільнення) робітників у плановому році.")
print("Чк = 2 *", str(CHvsixl), "-", str(CHp), "=", str(CHk))
print("Delta Ч найм. = ", str(CHk), "-", str(CHp), "=", "тут должен быть +", str(DeltaCHnaim))
print("")
print("")
print("3. Розрахувати продуктивність праці всіх і окремо основних робітників у звітному і плановому роках.")
print("ПП оз.вр = ", str(Vzv), "/", str(CHozvrr), "=", str(PPozvr))
print("ПП всіх = ", str(Vzv), "/", str(CHvsixv), "=", str(PPvsix))
print("ПП оп.лп. = ", str(Vpl), "/", str(CHoplrr), "=", str(PPoplr))
print("ПП всіхлп = ", str(Vpl), "/", str(CHvsixl), "=", str(PPvsixl))
print("")
print("")
print("4. Розрахувати додатковий приріст чи зниження обсягу виробництва за рахунок зміни чисельності і продуктивності "
      "праці окремо і в цілому.")
print("DeltaVchis = ", str(PPvsix), "* (", str(CHvsixl), "-", str(CHvsixv), ") =", str(DeltaVchis))
print("DeltaVpp = ", str(CHvsixl), "*(", str(PPvsixl), "-", str(PPvsix), ") =", str(DeltaVpp))
print("DeltaVppch =", str(DeltaVchis), "+", str(DeltaVpp), "=", str(DeltaVppch))
print("")
print("")
print("5. Розрахувати умовну економію чисельності основних і допоміжних робітників за рахунок росту продуктивності"
      " праці і обсягу виробництва.")
print("CHopprz = ", str(Vpl), "/", str(PPozvr), "=", str(CHopprz))
print("Eoppr = ", str(CHopprz), "-", str(CHoplrr), "=", str(Eoppr))
print("Edoppp = (", str(CHozvrr), "*", str(Vpl), "/", str(Vzv), ") - ", str(CHozvrr), "=", str(Edoppp))
print("")
print("")
print("6. Розрахувати оборот робочої сили за прийомом, оборот робочої сили за звільненням, коефіцієнт плинності та"
      " охарактеризувати за допомогою цих коефіцієнтів рух кадрів на даному підприємстві.")
print("Kop = ", str(CHp), "/",  str(CHvsixv), "=", str(Kop))
print("Koz = ", str(CHzvzag), "/",  str(CHvsixv), "=", str(Koz))
print("Kpl = ", str(CHzv), "/", str(CHvsixv), "=", str(Kpl))
