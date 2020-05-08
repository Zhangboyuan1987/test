import math
#曲柄销回转半径的计算
# S_i = 3048   #3048   2590.8   2159
# A = 3930
# I = 2840
# H = 5660
# G = 2510
# tol = 0
#
# lamda = 14
#
# K = math.sqrt(pow((H - G),2) + pow(I,2))
# print(K)   #k = 4241.24
#
# fai = math.atan(I/(H-G))
# print(fai)#hudu
#
# V_s12 = (S_i/A)*(180/math.pi)
# print(V_s12)#du
#
# theta = 180 - lamda
# print(theta)
#
# t1 = K * math.sin(math.radians(V_s12)/2)
# print(t1)
#
# t2 = math.sin((math.radians(theta)-math.radians(V_s12))/2)
# print(t2)
#
# t3 = math.cos(math.radians(180)-math.radians(theta)/2+math.radians(tol)-fai)
# print(t3)
#
# r = t1*t3/t2
# print(r)
    # R1 = 1054.98   876.04   716.11
    #       1060    880     750
#连杆长度的计算


# H = 5660
# G = 2510
# I = 2840
# R = 1060
# lamda = 14
#
# K = math.sqrt(pow((H - G),2) + pow(I,2))
# print(K)
#
# i = 2*K*math.sin(0.776/2)
# i = i**2
# print(i)
#
# c = math.cos(0.776+math.radians(lamda))
# print(c)
#
# m1 = i - 2*(R**2)*(1+c)
# print(m1)
#
# m2 = 2*(1-c)
#
# P = math.sqrt(m1/m2)
# print(P)
    #P = 2685.1         2685

#游梁后臂长度计算

# P = 2685
# R = 1060
# lamda = 14
#
# m1 =math.sin(math.radians(lamda)/2)**2
# print(m1)
# m2 =math.cos(math.radians(lamda)/2)**2
# print(m2)
# i = math.sin(0.776/2)**2
# print(i)
#
# C = math.sqrt((P**2 * m1 +R**2 * m2) / i)
# print(C)
    # C = 2912.24   2920

#实际冲
# 程计算

# C = 2920
# P = 2685
# R = 1060
# A = 3930
# K = 4241.24
#
# i1 =(C**2 + K**2 - (P+R)**2)/(2*C*K)
# print(i1)
# V_b = math.acos(i1)
#
# i2 =(C**2 + K**2 - (P-R)**2)/(2*C*K)
# V_t = math.acos(i2)
#
# S = (V_b-V_t)*A
# print(S)
    #s = 3050   2478    2091


#实际位移夹角
# P = 2685
# K = 4241.24
# C = 2912
# m1 = math.sin(0.776/2)
# m2 = math.cos(0.776/2)
# m3 = P**2 - K**2 * (m1**2)
# m4 = P**2 - C**2 * (m1**2)
# m5 = math.sqrt(m3/m4)
#
# lamda = 2*math.atan((m2-m5)/m1)
# print(math.degrees(lamda))
    #lamda = 14.0044

#基本尺寸计算结果
# ①游梁前臂长度 A                      154.72 in      (3930mm)
# ②游梁后臂长度 C                      114.65 in   (2912mm)
# ③支架轴承中心至底座底面之高度 H      222.83 in   (5660mm)
# ④减速器输出轴中心至底座底面之高度 G  98.82 in    (2510mm)
# ⑤减速器输出轴中心至支架轴承中心之水
# 平距离 I                              111.81 in    (2840mm)
# ⑥最大曲柄销回转半径 Rmax             41.73 in    (1060mm)
# ⑦连杆长度 P                          105.71 in  (2685mm)
# ⑧最大名义冲程长度 Smax               120 in      (3048mm)
# ⑨异相角：τ                           0°
# ⑩极位夹角λ             14.0044°

#光杆位置因数 PR 和扭矩因数 TF 的计算
# A = 3.930
# I1 = 2.840
# H = 5.660
# G = 2.510
# theta = 45
# R = 1.060
# K = 4.24124
# C = 2.912
# P = 2.685
#
# K = math.sqrt(pow((H - G),2) + pow(I1,2))
# print(K)
#
# theta_k = math.radians(theta) - math.atan(I1/(H-G))
# print(theta_k)
#
# print(math.sin(theta_k))
#
# J = math.sqrt(K**2 + R**2 - 2*K*R*math.cos(theta_k))
# print(J)
#
# Rou = math.asin((R*math.sin(theta_k))/J)
# print("ROU",Rou)
#
# print((C**2 + J**2 - P**2)/(2*C*J))
# X = math.acos((C**2 + J**2 - P**2)/(2*C*J))
# print(X)
#
# V = X - Rou
# print("v",V)
#
# print(J**2)
# b = math.acos((C**2+P**2-J**2)/(2*C*P))
# print("b",b)
#
# a = b + V - theta_k
# print("a",a)
#
# i1 = (C**2 + K**2 - (P+R)**2)/(2*C*K)
# V_b = math.acos(i1)
# print("V_b",V_b)
#
# i2 =(C**2 + K**2 - (P-R)**2)/(2*C*K)
# V_t = math.acos(i2)
# print(V_t)
#
# PR = (V_b - V)/(V_b - V_t)
#
# t1 = A*R/C
# t2 = math.sin(a)/math.sin(b)
#
# TF = t1*t2
# print(PR,TF)


#减速器参数
# 1.减速器形式：两级圆弧齿轮传动
# 2.传动比31.5
# 3对称分流式
# 4.中心距：850mm
# 额定输出转矩：36.155KN*m
# 润滑方式：飞溅式润滑
# 储油量：100L


#抽油机电机功率计算




#游梁结构件的强度校核计算
# A = 154.72
# I_z =5690.087716
# y_max = 30.71/2
# S_x = I_z/(y_max)
# print(S_x)
# J_e = 1.25*((2 * 11.81 * (0.87**3)) + (28.98 * (0.55**3)))*0.3333333
# print(J_e)
# I_y = 239.24750
# G = 11600000
# E = 29000000
# m1 = math.sqrt(G*I_y*E*J_e)
# m2 = S_x * A
# F_cb = m1/m2
# # F_cb = 11000
# print(F_cb)
#
#
# W = F_cb * S_x / A
#
# print(W)

#横梁结构件的强度校核计算
# W = 25600
# B = 1350
# A = 154.72
# C = 114.65
# b = 138.71
# W_x = 168
# P_lmax = (W-B)* A/(C* math.sin(math.radians(b)))
# print(P_lmax)
# F = 0.5 * P_lmax
# print(F)  #F = 24796.78
# theta_max = F * (73.3-14.96)/2 /W_x
#
# print(theta_max)


#连杆强度计算

F = 24796.78
S = 4.488
theat_pmax = F/S
print(theat_pmax)









