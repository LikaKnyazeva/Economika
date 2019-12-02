# Не изменяемые данные
NifA = 0.29
NifB = 0.16
NifC = 0.24
NifD = 0.31
NiplA = 0.3
NiplB = 0.15
NiplC = 0.23
NiplD = 0.32
priceA = 25
priceB = 30
priceC = 18
priceD = 45
CiB = 0.8 * 30
CiC = 0.73 * 18
CiD = 0.75 * 45
CiA = 0.78 * 25

# Изменяемые данные
# 1
Tpoct = 14
# 2
Tzp = 5
# 4
QchiA = 9
QchiB = 7
QchiC = 12
QchiD = 6
# 3
KmfA = 0.46
KmfB = 0.63
KmfC = 0.56
KmfD = 0.52
KmplA = 0.49
KmplB = 0.61
KmplC = 0.53
KmplD = 0.63
# 11
Nif = 230000
# 5
Nipl = 140000
# 6
Snozpl = 200000
# 7
Suzf = 168000
# 9
CoA = 25
CoB = 13
CoC = 12
CoD = 9

# Решения
# Маса (площа) і-го виду заготовки
QzifA = QchiA / KmfA
QzifB = QchiB / KmfB
QzifC = QchiC / KmfC
QzifD = QchiD / KmfD
QziplA = QchiA / KmplA
QziplB = QchiB / KmplB
QziplC = QchiC / KmplC
QziplD = QchiD / KmplD

# Сумарна потреба підприємства в певному матеріалі у натуральних одиницях:
Msf = Nif * NifA * QzifA + Nif * NifB * QzifB + Nif * NifC * QzifC + Nif * NifD * QzifD
Mspl = Nipl * NiplA * QziplA + Nipl * NiplB * QziplB + Nipl * NiplC * QziplC + Nipl * NiplD * QziplD

Df = Msf / 360
Dpl = Mspl / 360

# поточний запас
Zpotf = Df * Tpoct
Zpotpl = Dpl * Tpoct

# страховий запас
Zstrf = Df * Tzp
Zstrpl = Dpl * Tzp

# середній запас матеріалу
Zserf = Zstrf + 0.5 * Zpotf
Zserpl = Zstrpl + 0.5 * Zpotpl

# максимальний запас матеріалу:
Zmaxf = Zpotf + 0.5 * Zstrf
Zmaxpl = Zpotpl + 0.5 * Zstrpl

# Обсяг реалізованої продукції підприємства
Qrm = 25 * Nif * NifA + 30 * Nif * NifB + 18 * Nif * NifC + 45 * Nif * NifD
Qrpl = 25 * Nipl * NiplA + 30 * Nipl * NiplB + 18 * Nipl * NiplC + 45 * Nipl * NiplD

# коефіцієнт оборотності
Kobf = Qrm / Suzf
Kobpl = Qrpl / Snozpl

# тривалість одного обороту
Tobf = 360 / Kobf
Tobpl = 360 / Kobpl

# кількість днів скорочення періоду обороту оборотних засобів
Dscor = Tobf - Tobpl

# Абсолютне вивільнення
VOZa = Qrm / 360 * Dscor

# Відносне вивільнення
VOZv = 100 - (Qrpl / Qrm * 100)

# Повна собівартість всієї партії продукції
CvifpA = CiA * NifA
CvifpB = CiB * NifB
CvifpC = CiC * NifC
CvifpD = CiD * NifD
CviplA = CiA * NiplA
CviplB = CiB * NiplB
CviplC = CiC * NiplC
CviplD = CiC * NiplD

# сума поточних витрат у собівартості всієї партії виробів
CpifA = CvifpA - CoA
CpifB = CvifpB - CoB
CpifC = CvifpC - CoC
CpifD = CvifpD - CoD
CpiplA = CviplA - CoA
CpiplB = CviplB - CoB
CpiplC = CviplC - CoC
CpiplD = CviplD - CoD


# Вывод, що писать

print("1. Розрахувати потребу підприємства у матеріалі та його мінімальний,максимальний та середній запаси у поточному"
      " році (за планом і за фактом).")
print("Маса (площа) і-го виду заготовки")
print("q.зі.ф.А = ", str(QchiA), "/", str(KmfA), "=", str(QzifA))
print("q.зі.ф.Б = ", str(QchiB), "/", str(KmfB), "=", str(QzifB))
print("q.зі.ф.В = ", str(QchiC), "/", str(KmfC), "=", str(QzifC))
print("q.зі.ф.Д= ", str(QchiD), "/", str(KmfD), "=", str(QzifD))
print("q.зі.пл.А = ", str(QchiA), "/", str(KmplA), "=", str(QziplA))
print("q.зі.пл.Б = ", str(QchiB), "/", str(KmplB), "=", str(QziplB))
print("q.зі.пл.C = ", str(QchiC), "/", str(KmplC), "=", str(QziplC))
print("q.зі.пл.Д = ", str(QchiD), "/", str(KmplD), "=", str(QziplD))

print("Сумарна потреба підприємства в певному матеріалі у натуральних одиницях:")
print("М.с.ф = ", str(Nif), "*", str(NifA), "*", str(QzifA), "+", str(Nif), "*", str(NifB), "*", str(QzifB), "+",
      str(Nif), "*", str(NifC), "*", str(QzifC), "+", str(Nif), "*", str(NifD), "*", str(QzifD), "=", str(Msf))
print("М.с.пл = ", str(Nipl), "*", str(NiplA), "*", str(QziplA), "+", str(Nipl), "*", str(NiplB), "*", str(QziplB), "+",
      str(Nipl), "*", str(NiplC), "*", str(QziplC), "+", str(Nipl), "*", str(NiplD), "*", str(QziplD), "=", str(Mspl))
print("Дф = ", str(Msf), "/360", "=", str(Df))
print("Дпл = ", str(Mspl), "/360", "=", str(Dpl))

print("Cередній запас матеріалу")
print("З.сер.ф. = ", str(Zstrf), "+ 0.5*", str(Zpotf), "=", str(Zserf))
print("З.сер.пл. = ", str(Zstrpl), "+ 0.5*", str(Zpotpl), "=", str(Zserpl))
print("Максимальний запас матеріалу:")
print("З.мак.ф. = ", str(Zpotf), "+ 0.5*", str(Zstrf), "=", str(Zmaxf))
print("З.мак.пл. = ", str(Zpotpl), "+ 0.5*", str(Zstrpl), "=", str(Zmaxpl))

print("2. Розрахувати кількість днів скорочення періоду обороту оборотних засобів та абсолютну і відносну суму "
      "вивільнення оборотних засобів в цілому.")

print("Обсяг реалізованої продукції підприємства")
print("Q.р.м. = 25*", str(Nif), "*", str(NifA), "+ 30*", str(Nif), "*", str(NifB), "+ 18*", str(Nif), "*", str(NifC),
      "+ 45*", str(Nif), "*", str(NifD), "=", str(Qrm))
print("Q.р.пл. = 25*", str(Nipl), "*", str(NiplA), "+ 30*", str(Nipl), "*", str(NiplB), "+ 18*", str(Nipl), "*",
      str(NiplC), "+ 45*", str(Nipl), "*", str(NiplD), "=", str(Qrpl))

print("Коефіцієнт оборотності")
print("K.об.ф = ", str(Qrm), "/", str(Suzf), "=", str(Kobf))
print("K.об.пл = ", str(Qrpl), "/", str(Snozpl), "=", str(Kobpl))

print("тривалість одного обороту")
print("Т.об.ф. = 360/", str(Kobf), "=", str(Tobf))
print("Т.об.пл. = 360/", str(Kobpl), "=", str(Tobpl))

print("кількість днів скорочення періоду обороту оборотних засобів")
print("Д.скор =", str(Tobf), "-", str(Tobpl), "=", str(Dscor))

print("Абсолютне вивільнення")
print("ВОЗа = ", str(Qrm), "/360*", str(Dscor), "=", str(VOZa))

print("Відносне вивільнення")
print("ВОЗ% =  100 - (", str(Qrpl), "/", str(Qrm), "*100)", "=", str(VOZv))
