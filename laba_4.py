# Не изменяются
C1 = 25.13
Npl = 120
Kk = 6
Ksh = 5
Perev = 1.1
O = 7650
Vf = 18
Vpl = 22
K1 = 1
K2 = 1.09
K3 = 1.18
K4 = 1.27
K5 = 1.36
K6 = 1.45
# По особым таблицам
Pmin = 2
Pmax = 3
Kmin4 = 1.09
Kmax5 = 1.18
PPp = 40
# 2
Pser = 2.9
# 1
Tchi = 23.8
# 6
Nfi = 69
# 7
Nf = 198
# 4
Kchi114 = 1.5
# 3
Kchi113 = 1.3
# 8
Nf13 = 46
# 5
Kchi13 = 7.8

# Peшение
Ki = Kmin4 + (Pser - Pmin) * (Kmax5 - Kmin4)
Ci = C1 * Ki
Pzv = Tchi * Ci
Zpvidr = Pzv * Nfi

# Перший робітник
Ppp = (Nf - Npl)/Npl*100
Pzv111 = Ci * K3 * Kchi113
Zpvidr111 = Pzv111 * Nf
Dv1 = Zpvidr111 * (10+1.5*Ppp)/100
Zvprem1 = Zpvidr111 + Dv1

# другий робітник
Pzv112 = Ci * K4 * Kchi114
Zpvidr112 = Pzv112 * Nf
Dv2 = Zpvidr112*(10+1.5*Ppp)/100
Zvprem2 = Zpvidr112 + Dv2


Nvb = Kk*Ksh*Perev
Pzv113 = Ci * K5 * Kchi13
Pvb = (Nf13 - Nvb)/Nvb*100
Ppidv = Pzv113 * (1+PPp/100)
Zvprog= Nvb*Pzv113+(Nf13-Nvb)*Ppidv


Zpprem = O/Vf*Vpl*(1+(10+(20*2)/100))

# Вывод
print("1. Розрахувати розцінку за одну деталь К10 і загальний заробіток бригади по деталі К10. Проста відрядна система "
      "оплати праці.")
print("P сер. = ", str(Pser))
print("P мин. = ", str(Pmin))
print("P мах. = ", str(Pmax))
print("K мин. = ", str(Kmin4))
print("K мах. = ", str(Kmax5))
print("Ki = K мин. + (P сер.-P мин.)*(K мах.-K мин.)")
print("Ki = ", str(Kmin4), "+ (", str(Pser), "-", str(Pmin), " )*( ", str(Kmax5), "-", str(Kmin4), ") = ", str(Ki))
print("Ci = C1 * Ki")
print("Ci = ", str(C1), "*",  str(Ki), "=", str(Ci))
print("P зв. = T шт.і * Ci")
print("P зв. = ", str(Tchi), "*",  str(Ci), "=", str(Pzv))
print("З п.відр = P зв. * N ф.і")
print("З п.відр = ", str(Pzv), "*",  str(Nfi), "=", str(Zpvidr))
print("")
print("")
print("2. Розрахувати заробіток кожного робітника по деталі К11. Відрядно-преміальна система оплати праці. "
      "Премія за виконання плану 10% і за кожний відсоток перевиконання – 1,5%.")
print("")
print("Перший робітник")
print("N пл = 20 * 6")
print("П пп. =(Nф - N пл.)/N пл.*100")
print("П пп. = (", str(Nf), "-", str(Npl), ") /", str(Npl), "* 100", str(Ppp))
print("Pзв11(1) = ", str(Ci), "*", str(K3), "*", str(Kchi113), "=", str(Pzv111))
print("Зп.відр(1)= ", str(Pzv111), "*", str(Nf), "=", str(Zpvidr111))
print("Дв(1) = Зп.відр(1)* (П1+П2*Ппп)/100")
print("Дв(1) = ",  str(Zpvidr111), "* (10+1.5*", str(Ppp), ")/100 =", str(Dv1))
print("З в.прем (1) = Зп.відр(1)+ Дв(1)")
print("З в.прем (1) = ", str(Zpvidr111), "+", str(Dv1), "=", str(Zvprem1))
print("")
print("Другий робітник")
print("Pзв11(2) = ", str(Ci), "*", str(K4), "*", str(Kchi113), "=", str(Pzv111))
print("Зп.відр(2)= ", str(Pzv112), "*", str(Nf), "=", str(Zpvidr112))
print("Дв(2) = ",  str(Zpvidr112), "* (10+1.5*", str(Ppp), ")/100 =", str(Dv2))
print("З в.прем (2) = ", str(Zpvidr112), "+", str(Dv2), "=", str(Zvprem2))
print("")
print("")
print("3. Розрахувати заробіток робітника по деталі К13. Відрядно-прогресивна система оплати праці.")
print("Зв.прогр.=  N вб* Рзв+ ( N ф- N вб )* Рпідв.")
print("Nвб = ", str(Kk), "*", str(Ksh), "*", str(Perev), "=", str(Nvb))
print("Pзв = ", str(Ci), "*", str(K5), "*",  str(Kchi13), "=", str(Pzv113))
print("Пвб = (", str(Nf13), "-",  str(Nvb), ") /", str(Nvb), "*100 =", str(Pvb))
print("Ппп =", str(PPp))
print("Р.підв = ", str(Pzv113), "* (1+", str(PPp), "/100) =", str(Ppidv))
print("З.в. прогр= ", str(Nvb), "*", str(Pzv113), "+ (", str(Nf13), "-", str(Nvb), " )*", str(Ppidv), "=", str(Zvprog))
print("")
print("")
print("4. Розрахувати заробіток майстра дільниці за системою посадових окладів. Премія за виконання плану за комплекти "
      "(повні) - 20% і за кожний комплект понад план - 10%.")
print("Zpprem = ", str(O), "/", str(Vf), "*", str(Vpl), "*(1+(10+(20*2)/100))", "=", str(Zpprem))
