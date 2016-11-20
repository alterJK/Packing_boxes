# -*- coding: utf-8 -*-

# основная функция
def main():
    xData = []      #число данных
    yCount = []     #значения времени от числа прямоугольников
    yLength = []    #значения времени от длины большого прямоугольника
    yWeidth = []    #значения времени от ширины большого прямоугольника
#----------------------------------------------------------------------------
    file = open('DataCount.txt', 'r')
    for line in file:
        row = [float(i) for i in line.split()]
        xData.append(row[0])
        yCount.append(row[1])
    file.close()

    file = open('DataLength.txt', 'r')
    for line in file:
        row = [float(i) for i in line.split()]
        yLength.append(row[1])
    file.close()

    file = open('DataWeidth.txt', 'r')
    for line in file:
        row = [float(i) for i in line.split()]
        yWeidth.append(row[1])
    file.close()
#----------------------------------------------------------------------------
    #слияние в один файл
    with open('DATA.txt', 'w', encoding='utf-8') as f:
        for j in range(len(xData)):
            f.write(str(xData[j])+"\t"+str(yCount[j])+"\t"+
                    str(yLength[j])+"\t"+str(yWeidth[j])+"\n")

if __name__=='__main__':
    main()