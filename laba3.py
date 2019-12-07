# Данные которые не меняются
# Данные которые меняются
# 3
CHvsixv = 1358
# 4
Delta = 55.8
# 6
DeltaT = 69000
# 9
Fd = 1892
# 7
Fn = 259
# 5
CHp = 1538
# 10
DeltaKn = 7

# Решение

Kn = 1 + (DeltaKn / 100)  # 1
DeltaNop = DeltaT / (Fd * Kn)  # 2
CHozvrr = CHvsixv * (Delta / 100)  # 3
CHoplrr = CHozvrr - DeltaNop  # 4

Kcp = Fn / Fd  # 5
CHyavpl = CHoplrr / Kcp  # 6

CHdoplp = CHvsixv - CHozvrr  # 7
CHvsixl = CHoplrr + CHdoplp  # 8

CHk = 2*CHvsixl -CHp  # 10
DeltaCHnaim = CHk - CHp  # 11