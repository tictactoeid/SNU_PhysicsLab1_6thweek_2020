'''
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math'''
from exp12 import exp12
from exp3 import exp3
'''
# 큰 공 0.038m, 작은 공 0.0321m
BIGR = 0.038
SMALLR = 0.0321
# 큰 공 0.0542kg, 작은 공 0.0313 kg
BIGM = 0.0542
SMALLM = 0.0313
D = 0.0144 # 레일 사이의 간격
G = 9.8 #중력가속도'''

#print(HEIGHT, BALL_REFF)

exp1_1_1 = exp12(1, 1, '실험1.1_1', 75)
exp1_1_2 = exp12(1, 1, '실험1.1_2', 75)
exp1_1_3 = exp12(1, 1, '실험1.1_3', 75)
exp1_1_1.RUN()
exp1_1_2.RUN()
exp1_1_3.RUN()

exp1_2_1 = exp12(1, 2, '실험1.2_1', 85)
exp1_2_2 = exp12(1, 2, '실험1.2_2', 78)
exp1_2_3 = exp12(1, 2, '실험1.2_3', 90)
exp1_2_1.RUN()
exp1_2_2.RUN()
exp1_2_3.RUN()

exp2_1_1 = exp12(2, 1, '실험2.1_1', 73)
exp2_1_2 = exp12(2, 1, '실험2.1_2', 55)
exp2_1_3 = exp12(2, 1, '실험2.1_3', 60)
exp2_1_1.RUN()
exp2_1_2.RUN()
exp2_1_3.RUN()

exp2_2_1 = exp12(2, 2, '실험2.2_1', 55)
exp2_2_2 = exp12(2, 2, '실험2.2_2', 60)
exp2_2_3 = exp12(2, 2, '실험2.2_3', 65)
exp2_2_1.RUN()
exp2_2_2.RUN()
exp2_2_3.RUN()
'''exp3_1_5 = exp3(1, '실험3.1_5', 93) #rows = 30이면 Excel file의 30번 행부터
exp3_1_6 = exp3(1, '실험3.1_6', 96)
exp3_1_7_1 = exp3(1, '실험3.1_7_1', 91)
exp3_1_7_2 = exp3(1, '실험3.1_7_2', 96)
exp3_1_8_1 = exp3(1, '실험3.1_8_1', 88)
exp3_1_8_2 = exp3(1, '실험3.1_8_2', 93)

exp3_1_5.RUN()
exp3_1_6.RUN()
exp3_1_7_1.RUN()
exp3_1_7_2.RUN()
exp3_1_8_1.RUN()
exp3_1_8_2.RUN()'''

