import random
import matplotlib.pyplot as plt
import math
import numpy as np


class CountryX:
    def __init__(self, mu=1, epsilon=1, petrol_station_num=100):
        # 随机初始化每个加油站的坐标
        self.petrol_station = []
        self.mask_petrol_station = []
        for i in range(petrol_station_num):
            self.petrol_station.append(
                (random.random()*1000, random.random()*1000)
            )
        self.mu = mu
        self.epsilon = epsilon
        self.value = 0
        self.count = 0

    def query(self, L, R, D, U):
        # 数据接口
        num = 0
        value = np.random.laplace(self.mu, self.epsilon, 1)[0]
        self.value += (value)
        self.count += 1
        for x, y in self.petrol_station:
            if x >= L and x <= R and y >= D and y <= U:
                num += 1
        return num + value
        #
        # for x, y in self.mask_petrol_station:
        #     if x >= L and x <= R and y >= D and y <= U:
        #         num += 1
        # return num

    def launch_missile(self, missile_x, missile_y, explosion_radius=1, show=False):
        # 在坐标(missile_x, missile_y)处发射导弹，并判断是否波及某一加油站
        if show:
            self.show()
            plt.scatter(x=[missile_x], y=[missile_y], label="missile")
            plt.legend()
        for x, y in self.petrol_station:
            distance = math.sqrt(
                (x-missile_x)*(x-missile_x)+(y-missile_y)*(y-missile_y))
            if distance <= explosion_radius:
                return True
        return False

    def show(self):
        # 展示所有加油站的位置
        plt.figure()
        plt.scatter(
            x=[i[0] for i in self.petrol_station],
            y=[i[1] for i in self.petrol_station],
            label="petrol station"
        )
        plt.xlim(-100, 1100)
        plt.ylim(-100, 1100)
        plt.legend()
        #plt.show()

    def laplace(self, mu, epsilon):
        for i in self.petrol_station:
            i = list(i)
            laplace_value = np.random.laplace(mu, epsilon, 2)
            i[0] += laplace_value[0]
            i[1] += laplace_value[1]
            self.mask_petrol_station.append(
                (i[0],i[1])
            )

    def computer_distance(self):
        distance = 0
        for i in range(len(self.petrol_station)):
            x0, y0, x1, y1 = self.petrol_station[i][0], self.petrol_station[i][1], self.mask_petrol_station[i][0], self.mask_petrol_station[i][1]
            distance += math.sqrt((x0 - x1)**2 + (y0 - y1)**2)

        return distance / len(self.petrol_station)

    def print(self):
        return self.value / self.count

def SpyProgram(data_api):
    # 间谍程序，用二分法缩小范围，找到其中一个加油站
    L, R, D, U = 0, 1000, 0, 1000
    while True:
        if random.randint(0, 1) == 0:
            M = (L+R)/2
            num1 = data_api.query(L, M, D, U)
            num2 = data_api.query(M, R, D, U)
            if num1 > num2:
                R = M
            else:
                L = M
        else:
            M = (D+U)/2
            num1 = data_api.query(L, R, D, M)
            num2 = data_api.query(L, R, M, U)
            if num1 > num2:
                U = M
            else:
                D = M
        # 当范围足够小时，结束程序，准备发射导弹
        if R-L <= 1 and U-D <= 1:
            break
    return (L+R)/2, (D+U)/2

mu = np.arange(0,11,1)
res = []
distance = []
print(mu)
print(np.random.laplace(0, 1, 2))
for i in mu:
    count = 0
    # X国模拟器
    countryX = CountryX(mu=i, epsilon=1)
    # 展示X国内所有加油站的位置
    countryX.show()
    # countryX.laplace(0, i)

    # 模拟间谍行为，根据间谍程序得到的坐标，导弹百发百中
    for i in range(100):
        x, y = SpyProgram(countryX)
        if countryX.launch_missile(x, y):
            count += 1
        #     print("导弹命中")
        # else:
        #     print("导弹未命中")

    print(countryX.print(),countryX.value,countryX.count)
    res.append(count / 100)
    # distance.append(countryX.computer_distance())
    print("命中数{}/100,总命中率{}".format(count, count / 100))
    # print(countryX.computer_distance())

print(res,distance)