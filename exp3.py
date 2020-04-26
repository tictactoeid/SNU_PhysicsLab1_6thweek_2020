
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

# 큰 공 0.038m, 작은 공 0.0321m
BIGR = 0.038
SMALLR = 0.0321
# 큰 공 0.0542kg, 작은 공 0.0313 kg
BIGM = 0.0542
SMALLM = 0.0313
D = 0.0144 # 레일 사이의 간격
G = 9.8 #중력가속도

#print(HEIGHT, BALL_REFF)

class exp3(): #실험 1,2: 직선 궤도에서 공의 역학적 에너지 보존 확인
    def __init__(self, ballType, sheet, rows):
        #rows: 분석할 행 수. 직선 궤도 영역만 분석하므로,
        #Excel에서 x가 감소하기 직전의 행 번호를 입력하고, x-y그래프 보고 직선이 되도록 조정

        #실험 변인
        file = 'raw_3.xlsx'
        self.HEIGHT = round(0.83 * math.sin(math.radians(30)), 5) #전체 궤도 높이
        if ballType == 1: #실험 3.1 큰 공
            self.BALL_R = BIGR #공의 반지름
            self.BALL_MASS = BIGM #공의 질량
        elif ballType == 2: # 실험 3.2 작은 공
            self.BALL_R = SMALLR
            self.BALL_MASS = SMALLM
        self.BALL_REFF = round(math.sqrt(self.BALL_R ** 2 - D ** 2), 5) #공의 유효반지름
        self.title = sheet[2:5] + " " + sheet[6] + "cm" + sheet[7:] #ex) 실험3.1_5, 실험3.1_7_1

        #pandas DataFrame으로 데이터를 저장.
        self.data = pd.read_excel(file, sheet_name = sheet, dtype={'t': float, 'x': float, 'y': float}, header=2) #원본 raw data
        if __name__ == "__main__": # test
            print(self.data)
        self.data = self.data.loc[rows - 4:] # 원운동 구간만 분석하므로, 직선운동 구간을 제거.
        if __name__ == "__main__": # test
            print(self.data)

    def drawGraph(self, xdata, ydata, save = True, show = True, **labels):
        if "range" in labels:
            plt.plot(xdata[:range], ydata[:range])
        else:
            plt.plot(xdata, ydata)
        if "xlabel" in labels:
            plt.xlabel(labels["xlabel"])
        if "ylabel" in labels:
            plt.ylabel(labels["ylabel"])

        plt.title(self.title)

        if save:
            plt.savefig(self.title + ".png")
        if show:
            plt.show()


    def RUN(self, saveGraph = False, showGraph = True, **optionalRange): #코드를 실행
        if "range" in optionalRange:
            self.drawGraph(self.data['x'], self.data['y'], save = saveGraph, show= showGraph, range = optionalRange['range'])
        else:
            self.drawGraph(self.data['x'], self.data['y'], save = saveGraph, show= showGraph)

if __name__ == '__main__':
    exp3_1_5 = exp3(1, '실험3.1_5', 30) #rows = 30이면 Excel file의 30번 행부터
