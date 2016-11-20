# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 19:16:28 2016

@author: vital
"""

# основная функция
def main():
    COUNT = [5, 10, 50, 100, 500, 1000, 5000, 10000]
    nameCount = 'testCount'
    nameWeidth = 'testWeidth'
    nameLength = 'testLength'
    for i in range(len(COUNT)):
        #формирование теста числа данных
        filename = nameCount +str(COUNT[i])+'.txt'
        with open(filename, 'a', encoding='utf-8') as f:
            n = COUNT[i]
            f.write(str(100)+"\t"+str(1)+"\n")
            for j in range(n-1):
                f.write(str(1)+"\t"+str(1)+"\n")
        #формирование теста ширины большого прямоугольника
        filename = nameWeidth +str(COUNT[i])+'.txt'
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(str(n)+"\t"+str(1)+"\n")
            for j in range(4):
                f.write(str(1)+"\t"+str(1)+"\n")
        #формирование теста длины большого прямоугольника
        filename = nameLength +str(COUNT[i])+'.txt'
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(str(1)+"\t"+str(n)+"\n")
            for j in range(4):
                f.write(str(1)+"\t"+str(1)+"\n")

if __name__=='__main__':
    main()