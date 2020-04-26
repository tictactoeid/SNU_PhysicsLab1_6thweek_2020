
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

class exp12(): #실험 1,2: 직선 궤도에서 공의 역학적 에너지 보존 확인
    def __init__(self, expType, ballType, sheet, rows):
        #rows: 분석할 행 수. 직선 궤도 영역만 분석하므로,
        #Excel에서 x가 감소하기 직전의 행 번호를 입력하고, x-y그래프 보고 직선이 되도록 조정

        #실험 변인
        if expType == 1: # 실험 1(30도)
            file = 'raw_1.xlsx'
            self.HEIGHT = round(0.83 * math.sin(math.radians(30)), 5) #전체 궤도 높이
        elif expType == 2: #실험 2(40도)
            file = 'raw_2.xlsx'
            self.HEIGHT = round(0.83 * math.sin(math.radians(40)), 5)
        if ballType == 1: #실험 1.1, 2.1 등 큰 공
            self.BALL_R = BIGR #공의 반지름
            self.BALL_MASS = BIGM #공의 질량
        elif ballType == 2: # 실험 1.2, 2.2 등 작은 공
            self.BALL_R = SMALLR
            self.BALL_MASS = SMALLM
        self.BALL_REFF = round(math.sqrt(self.BALL_R ** 2 - D ** 2), 5) #공의 유효반지름
        self.title = sheet[2:5] + "." + sheet[-1] #ex) 실험1.1_1

        #pandas DataFrame으로 데이터를 저장.
        self.data = pd.read_excel(file, sheet_name = sheet, dtype={'t': float, 'x': float, 'y': float}, header=3,
                             nrows = rows) #원본 raw data
        self.newdata = pd.DataFrame(index=range(0, rows),
                                    columns=['t', 'x', 'y', 'deltat', 'deltax', 'deltay', 'mechE'])
        #원본 raw data에서 x의 변화, y의 변화, 시간 변화, 역학적 에너지를 추가

    def mechEnergy(self, xi, xf, deltax, deltay, deltat): #두 구간 사이 평균 역학적 에너지를 계산
        #데이터에서 x는 아래, y는 오른쪽 방향
        vCom = (deltax ** 2 + deltay ** 2) / deltat ** 2 # 질량중심 선속도의 제곱
        h = (self.HEIGHT - (xf + xi) / 2) #지면이 높이 0이 되도록 높이를 변환
        a = 0.5 + (self.BALL_R**2 / 5 * (self.BALL_REFF ** 2)) #회전운동을 고려한 운동에너지에서 v^2 계수
        return self.BALL_MASS*(a*vCom + G*h)

    def mechEnergyTheorical(self):
        value = self.BALL_MASS * G * self.HEIGHT
        yAxisValue = []
        for i in range(len(self.data['t'])):
            yAxisValue.append(value)
        return yAxisValue

    def updateData(self):
        self.newdata['t'] = self.data['t']
        self.newdata['x'] = self.data['x']
        self.newdata['y'] = self.data['y']

        for i in range(len(self.data['t']) - 1): # delta x와 delta y를 계산
            #print(data['x'][i])
            self.newdata['deltax'][i] = self.data['x'][i+1] - self.data['x'][i]
            self.newdata['deltay'][i] = self.data['y'][i+1] - self.data['y'][i]
            self.newdata['deltat'][i] = self.data['t'][i+1] - self.data['t'][i]

        for i in range(len(self.data['t']) - 1): # 각 지점의 역학적 에너지를 계산
            self.newdata['mechE'][i] = self.mechEnergy(self.data['x'][i], self.data['x'][i+1], self.newdata['deltax'][i], self.newdata['deltay'][i], self.newdata['deltat'][i])


        #print(self.data)
        #print(self.newdata)
        #print(self.newdata['t'], self.newdata['mechE'])

    def drawGraph(self, xdata, ydata, save = True, show = True, **labels):
        if "range" in labels:
            plt.plot(xdata[:range], ydata[:range])
        else:
            plt.plot(xdata, ydata)
        #plt.plot(xdata, self.mechEnergyTheorical())
        #역학적 에너지의 이론값
        if "xlabel" in labels:
            plt.xlabel(labels["xlabel"])
        if "ylabel" in labels:
            plt.ylabel(labels["ylabel"])
        if "title" in labels:
            plt.title(labels["title"])
        if save:
            plt.savefig(labels["title"] + ".png")
        if show:
            plt.show()


    def RUN(self, saveGraph = True, showGraph = True, **optionalRange): #코드를 실행
        self.updateData()
        if "range" in optionalRange:
            self.drawGraph(self.newdata['t'], self.newdata['mechE'], save = saveGraph, show = showGraph, xlabel='time', ylabel='Mechanical Energy',
                       title=self.title, range = optionalRange['range'])
        else:
            self.drawGraph(self.newdata['t'], self.newdata['mechE'], xlabel='time (s)', ylabel='Mechanical Energy (J)',
                           title=self.title)

        self.drawGraph(self.newdata['x'], self.newdata['y'], title=self.title + " x-y")

if __name__ == '__main__':
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
