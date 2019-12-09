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
Tpoct = 18
# 2
Tzp = 6
# 4
QchiA = 12
QchiB = 9
QchiC = 15
QchiD = 7
# 3
KmfA = 0.59
KmfB = 0.81
KmfC = 0.71
KmfD = 0.79
KmplA = 0.63
KmplB = 0.78
KmplC = 0.68
KmplD = 0.81
# 11
Nif = 231000
# 5
Nipl = 180000
# 6
Snozpl = 74000
# 7
Suzf = 61200
# 9
CoA = 32
CoB = 17
CoC = 12
CoD = 15
# 8
TcA = 7
TcB = 15
TcC = 12
TcD = 9

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
Zmaxf = Zpotf + Zstrf
Zmaxpl = Zpotpl + Zstrpl

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
Dscor = (Tobf - Tobpl)*(-1)

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

# Коефіцієнт наростання витрат
KifA = (CoA + 0.5*CpifA)/(CoA+CpifA)
KifB = (CoB + 0.5*CpifB)/(CoB+CpifB)
KifC = (CoC + 0.5*CpifC)/(CoC+CpifC)
KifD = (CoD + 0.5*CpifD)/(CoD+CpifD)

KiplA = (CoA + 0.5*CpiplA)/(CoA+CpiplA)
KiplB = (CoB + 0.5*CpiplB)/(CoB+CpiplB)
KiplC = (CoC + 0.5*CpiplC)/(CoC+CpiplC)
KiplD = (CoD + 0.5*CpiplD)/(CoD+CpiplD)

# Норму запасу оборотних фондів

HifA = (CiA*NifA*TcA*KifA)/360
HifB = (CiB*NifB*TcB*KifB)/360
HifC = (CiC*NifC*TcC*KifC)/360
HifD = (CiD*NifD*TcD*KifD)/360
HiplA = (CiA*NiplA*TcA*KiplA)/360
HiplB = (CiB*NiplB*TcB*KiplB)/360
HiplC = (CiC*NiplC*TcC*KiplC)/360
HiplD = (CiD*NiplD*TcD*KiplD)/360

# коефіцієнт завантаження
Kzavf = Suzf/Qrm
Kzavpl = Snozpl/Qrpl

# матеріаловіддача
Mvf = Qrm/Msf
Mvpl = Qrpl/Mspl

# Коефіцієнт використання матеріалів
Kvukmf = (NifA*QchiA+NifB*QchiB+NifC*QchiC+NifD*QchiD)/Msf
Kvukmpl = (NiplA*QchiA+NiplB*QchiB+NiplC*QchiC+NiplD*QchiD)/Mspl

# Вывод, що писать

print("1. Розрахувати потребу підприємства у матеріалі та його мінімальний,максимальний та середній запаси у поточному"
      " році (за планом і за фактом).")
print("Маса (площа) і-го виду заготовки")
print("q.зі.ф.А = ", str(QchiA), "/", str(KmfA), "=", str(QzifA))
print("q.зі.ф.Б = ", str(QchiB), "/", str(KmfB), "=", str(QzifB))
print("q.зі.ф.В = ", str(QchiC), "/", str(KmfC), "=", str(QzifC))
print("q.зі.ф.Г = ", str(QchiD), "/", str(KmfD), "=", str(QzifD))
print("q.зі.пл.А = ", str(QchiA), "/", str(KmplA), "=", str(QziplA))
print("q.зі.пл.Б = ", str(QchiB), "/", str(KmplB), "=", str(QziplB))
print("q.зі.пл.В = ", str(QchiC), "/", str(KmplC), "=", str(QziplC))
print("q.зі.пл.Г = ", str(QchiD), "/", str(KmplD), "=", str(QziplD))

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
print("З.мак.ф. = ", str(Zpotf), "+", str(Zstrf), "=", str(Zmaxf))
print("З.мак.пл. = ", str(Zpotpl), "+", str(Zstrpl), "=", str(Zmaxpl))

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

print("3. Розрахувати норму запасу оборотних фондів у незавершеному виробництві"
      "по кожному виробу (за планом і за фактом).")

print("Повна собівартість всієї партії продукції")
print("С.ві.фп.А = ", str(CiA), "*", str(NifA), "=", str(CvifpA))
print("С.ві.фп.Б = ", str(CiB), "*", str(NifB), "=", str(CvifpB))
print("С.ві.фп.В = ", str(CiC), "*", str(NifC), "=", str(CvifpC))
print("С.ві.фп.Г = ", str(CiD), "*", str(NifD), "=", str(CvifpD))
print("С.ві.пл.А = ", str(CiA), "*", str(NiplA), "=", str(CviplA))
print("С.ві.пл.Б = ", str(CiB), "*", str(NiplB), "=", str(CviplB))
print("С.ві.пл.В = ", str(CiC), "*", str(NiplC), "=", str(CviplC))
print("С.ві.пл.Г = ", str(CiD), "*", str(NiplD), "=", str(CviplD))

print("сума поточних витрат у собівартості всієї партії виробів")
print("C.пі.ф.А = ", str(CvifpA), "-", str(CoA), "=", str(CpifA))
print("C.пі.ф.Б = ", str(CvifpB), "-", str(CoB), "=", str(CpifB))
print("C.пі.ф.В = ", str(CvifpC), "-", str(CoC), "=", str(CpifC))
print("C.пі.ф.Г = ", str(CvifpD), "-", str(CoD), "=", str(CpifD))
print("C.пі.пл.А = ", str(CviplA), "-", str(CoA), "=", str(CpiplA))
print("C.пі.пл.Б = ", str(CviplB), "-", str(CoB), "=", str(CpiplB))
print("C.пі.пл.В = ", str(CviplC), "-", str(CoC), "=", str(CpiplC))
print("C.пі.пл.Г = ", str(CviplD), "-", str(CoD), "=", str(CpiplD))

print("Коефіцієнт наростання витрат")
print("К.і.ф.А= ( ", str(CoA), "+ 0.5*", str(CpifA), ")/(", str(CoA), "+", str(CpifA), "=", str(KifA))
print("К.і.ф.Б= ( ", str(CoB), "+ 0.5*", str(CpifB), ")/(", str(CoB), "+", str(CpifB), "=", str(KifB))
print("К.і.ф.В= ( ", str(CoC), "+ 0.5*", str(CpifC), ")/(", str(CoC), "+", str(CpifC), "=", str(KifC))
print("К.і.ф.Г= ( ", str(CoD), "+ 0.5*", str(CpifD), ")/(", str(CoD), "+", str(CpifD), "=", str(KifD))
print("К.і.пл.А= ( ", str(CoA), "+ 0.5*", str(CpiplA), ")/(", str(CoA), "+", str(CpiplA), "=", str(KiplA))
print("К.і.пл.Б= ( ", str(CoB), "+ 0.5*", str(CpiplB), ")/(", str(CoB), "+", str(CpiplB), "=", str(KiplB))
print("К.і.пл.В= ( ", str(CoC), "+ 0.5*", str(CpiplC), ")/(", str(CoC), "+", str(CpiplC), "=", str(KiplC))
print("К.і.пл.Г= ( ", str(CoD), "+ 0.5*", str(CpiplD), ")/(", str(CoD), "+", str(CpiplD), "=", str(KiplD))

print("Норму запасу оборотних фондів")
print("H.і.ф.А = ( ", str(CiA), "*", str(NifA), "*", str(TcA), "*", str(KifA), ")/360", "=", str(HifA))
print("H.і.ф.Б = ( ", str(CiB), "*", str(NifB), "*", str(TcB), "*", str(KifB), ")/360", "=", str(HifB))
print("H.і.ф.В = ( ", str(CiC), "*", str(NifC), "*", str(TcC), "*", str(KifC), ")/360", "=", str(HifC))
print("H.і.ф.Г = ( ", str(CiD), "*", str(NifD), "*", str(TcD), "*", str(KifD), ")/360", "=", str(HifD))
print("Н.і.пл.А = (", str(CiA), "*", str(NiplA), "*", str(TcA), "*", str(KiplA), ")/360", "=", str(HiplA))
print("Н.і.пл.Б = (", str(CiB), "*", str(NiplB), "*", str(TcB), "*", str(KiplB), ")/360", "=", str(HiplB))
print("Н.і.пл.В = (", str(CiC), "*", str(NiplC), "*", str(TcC), "*", str(KiplC), ")/360", "=", str(HiplC))
print("Н.і.пл.Г = (", str(CiD), "*", str(NiplD), "*", str(TcD), "*", str(KiplD), ")/360", "=", str(HiplD))


print("4.Розрахувати коефіцієнт завантаження (за планом і за фактом).")


print("коефіцієнт завантаження")
print("K.зав.ф.= ", str(Suzf), "/", str(Qrm), "=", str(Kzavf))
print("K.зав.пл.= ", str(Snozpl), "/", str(Qrpl), "=", str(Kzavf))


print("5. Розрахувати загальну матеріалоємність та матеріаловіддачу, загальний"
      "коефіцієнт використання матеріалу в цілому по підприємству (за планом і зa фактом).")


print("матеріаловіддача")
print("Mв.ф = ", str(Qrm), "/", str(Msf), "=", str(Mvf))
print("Mв.пл = ", str(Qrpl), "/", str(Mspl), "=", str(Mvpl))

print("Коефіцієнт використання матеріалів")
print("К.вик.матер.ф = (", str(NifA), "*", str(QchiA), "+", str(NifB), "*", str(QchiB), "+", str(NifC), "*", str(QchiC),
      "+", str(NifD), "*", str(QchiD), "/", str(Msf), "=", str(Kvukmf))
print("К.вик.матер.пл = (", str(NiplA), "*", str(QchiA), "+", str(NiplB), "*", str(QchiB), "+", str(NiplC), "*",
      str(QchiC), "+", str(NiplD), "*", str(QchiD), "/", str(Mspl), "=", str(Kvukmpl))
