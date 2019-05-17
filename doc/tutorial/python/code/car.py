# class AccordCar:    
#     brand  = 'Accord'
#     maxspeed = 200
#     price   = 180000

#     @staticmethod
#     def pressHorn(): 
#         print('嘟嘟~~~~~~')

#     def __init__(self,color,engineSN):
#         self.color  =  color  # 颜色
#         self.engineSN = engineSN # 发动机编号
    
#     def changeColor(self,newColor):
#         self.color = newColor

# class AccordCar2016(AccordCar):
#     model = 'Accord2016'


# class AccordCar2018(AccordCar):
#     model = 'Accord2018'  

#     def __init__(self,color,engineSN,weight):
#         AccordCar.__init__(self,color,engineSN)
#         self.weight = weight # 重量
#         self.oilweight = 0  # 油的重量
    
#     # 加油
#     def fillOil(self, oilAdded):
#         self.oilweight +=  oilAdded 
#         self.weight    +=  oilAdded
        


# class AccordCar2018Hybrid(AccordCar2018):
#     model = 'Accord2018Hybrid' 
    
#     def __init__(self,color,engineSN,weight):
#         AccordCar2018.__init__(self,color,engineSN,weight)


 
# car2 = AccordCar2018Hybrid('blue','111135545988',1500)   
# print (car2.oilweight)
# print (car2.weight)
# car2.fillOil(50) 
# print (car2.oilweight)
# print (car2.weight)



class Tire:    
    def __init__(self,size,createDate):
        self.size  =  size  # 尺寸
        self.createDate = createDate # 出厂日期

class AccordCar:    
    brand  = 'Accord'
    maxspeed = 200
    price   = 180000

  
    def __init__(self,color,engineSN,tires):
        self.color  =  color  # 颜色
        self.engineSN = engineSN # 发动机编号
        self.tires   =  tires

# 创建4个轮胎实例对象
tires = [Tire(20,'20160808')  for i in range(4)]
car = AccordCar('red','234342342342566',tires)

print(car.tires)