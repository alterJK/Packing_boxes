# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""

import numpy
import matplotlib.pyplot as plt

#-------------------------------------------------------------------
xData = []      #число данных
yCount = []     #значения времени от числа прямоугольников
yLength = []    #значения времени от длины большого прямоугольника
yWeidth = []    #значения времени от ширины большого прямоугольника
#------------------------------------------------------------------

# пострение графиков
def graphics_build():
    pass
    #массив значений аргумента
    x = numpy.arange( 0, 10.01, 0.01 )
    x = numpy.array(xData, dtype=float)
    #массивы значений функции
    y1 = numpy.array(yCount, dtype=float)
#    y2 = numpy.array(yLength, dtype=float)
#    y3 = numpy.array(yWeidth, dtype=float)
    #Построение графика
    plt.plot(x,y1)
    #Метка по оси x в формате TeX
    plt.xlabel(r'$Изменение\ данных$')
    #Метка по оси y в формате TeX
    plt.ylabel(r'$Время\ выполнения$')
    #Заголовок в формате TeX
    plt.title(r'$Сложность\ алгоритма$')
    plt.grid(True) #Сетка
    plt.show()#Показать график


# чтение из файла
def write_from_file():
    file = open('DATA.txt', 'r') #файл для считывания параметров прямоугольников
    for line in file:
        row = [float(i) for i in line.split()]
        xData.append(row[0])
        yCount.append(row[1])
#        yLength.append(row[2])
#        yWeidth.append(row[3])
    file.close()

# основная функция
def main():
    write_from_file()
    graphics_build()


if __name__=='__main__':
    main()

