from math import sqrt, pi

##.i
class RegressionCalculator:
    def __init__ (self, xk: int):
        self.__pairsN = 0
        self.__x_sum = 0.00
        self.__y_sum = 0.00
        self.__x2_sum = 0.00
        self.__y2_sum = 0.00
        self.__xy_sum = 0.00
        self.__xk = xk
    
    def addPair (self, x:float, y:float):
        self.__pairsN += 1
        self.__x_sum += x
        self.__y_sum += y
        self.__x2_sum += x*x
        self.__y2_sum += y*y
        self.__xy_sum += x*y

    def calc_r (self):
        numerator = self.__pairsN*self.__xy_sum-self.__x_sum*self.__y_sum
        denominator = sqrt((self.__pairsN*self.__x2_sum-(self.__x_sum ** 2))*(self.__pairsN*self.__y2_sum-(self.__y_sum ** 2)))
        return numerator / denominator

    def calc_r2 (self, r:float = None):
        if not r: r = self.calc_r()
        return (r*r)
    
    def calc_b1 (self):
        yavg = self.__y_sum / self.__pairsN
        xavg = self.__x_sum / self.__pairsN
        numerator = self.__xy_sum-(self.__pairsN*xavg*yavg)
        denominator = self.__x2_sum-(self.__pairsN*(xavg ** 2))
        return numerator / denominator
    
    def calc_b0 (self, b1:float = None):
        yavg = self.__y_sum / self.__pairsN
        xavg = self.__x_sum / self.__pairsN
        if not b1: b1 = self.calc_b1()
        return yavg - b1*xavg
    
    def calc_yk (self: int, b0:float = None, b1:float = None):
        if not b0: b0 = self.calc_b0()
        if not b1: b1 = self.calc_b1()
        yk = b0 + b1*self.__xk
        return yk
    
    def __repr__ (self):
        r = self.calc_r()
        r2 = self.calc_r2(r)
        b1 = self.calc_b1()
        b0 = self.calc_b0(b1)
        yk = self.calc_yk(b0,b1)
        result = f"N = {self.__pairsN}\nxk = {self.__xk}\n{r = :.5f}\n{r2 = :.5f}\n{b0 = :.5f}\n{b1 = :.5f}\n{yk = :.5f}\n"
        return result