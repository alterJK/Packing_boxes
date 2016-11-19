import time

WIDTHS = [] #массив ширины
LENGTHS = [] #массив длины
SQUARES = [] #площади прямоугольников
    
coordinates = []#лист для хранения координат
fl_turn = False #флаг использования поворота
first_w_coord = []
first_l_coord = []


#проверка предполагаемой первой координаты
def check_busy_coordinates(coord_w, coord_l, kol, current_w, current_l):
    #проверка на то, что точка является первой 
    #координатой вписанного прямоугольника
    if ((coord_w<WIDTHS[0] and coord_l<LENGTHS[0]) and
        (coord_w+current_w-1<WIDTHS[0] and coord_l+current_l-1<LENGTHS[0]) and
        (coord_w>=0 and coord_l>=0)):
        for i in range(kol-1):
            #проверка на совпадение с первой координатой
            if (coord_w == first_w_coord[i] and coord_l == first_l_coord[i]):
                return False
        #проверка на наложение на вписанные прямоугольники        
        for i in range(kol-1):
            if (
                #проверка первой координаты вписываемого прямогольника                
                ((coord_w>=coordinates[i][0][0]) and (coord_w<=coordinates[i][1][0]) and
                 (coord_l>=coordinates[i][0][1]) and (coord_l<=coordinates[i][1][1])) or
                #проверка второй координаты вписываемого прямогольника
                ((coord_w+current_w-1>=coordinates[i][0][0]) and (coord_w+current_w-1<=coordinates[i][1][0]) and
                 (coord_l+current_l-1>=coordinates[i][0][1]) and (coord_l+current_l-1<=coordinates[i][1][1]))
                ):
                return False
    else:
        return False
    return True
    
    
#поиск свободного места    
def find_place(count, kol, current_w, current_l):
    for i in range(kol-1):       
        #если справа есть свободное место или вписанных только один
        if (check_busy_coordinates(coordinates[i][0][0],coordinates[i][1][1]+1, 
                                   kol, current_w, current_l) or (kol == 1)):
            #если уместится по ширине и длине
            if ((WIDTHS[0]-coordinates[i][0][0]>=current_w) and
                (LENGTHS[0]-coordinates[i][1][1]>=current_l)):
                coordinates.append([[coordinates[i][0][0],
                                     coordinates[i][1][1]+1],
                                    [coordinates[i][0][0]+current_w-1,
                                     coordinates[i][1][1]+current_l]])
                first_w_coord.append(coordinates[i][0][0])
                first_l_coord.append(coordinates[i][1][1]+1)
                return True       
        if (check_busy_coordinates(coordinates[i][1][0]+1,coordinates[i][0][1], 
                                   kol, current_w, current_l) or (kol == 1)):
            #если уместится по ширине и длине
            if ((WIDTHS[0]-coordinates[i][1][0]-1>=current_w) and
                ((LENGTHS[0]-coordinates[i][0][1]-1>=current_l) or
                 (LENGTHS[0]-coordinates[i][0][1]-1 >= 0))):
                #проверка на свободное место слева от предполагаемой начальной координаты
                fl_new = check_busy_coordinates(coordinates[i][1][0]+1,coordinates[i][0][1]-1, 
                                                kol, current_w, current_l)
                if (fl_new==False):
                    coordinates.append([[coordinates[i][1][0]+1,
                                         coordinates[i][0][1]],
                                        [coordinates[i][1][0]+current_w,
                                         coordinates[i][0][1]+current_l-1]])
                    first_w_coord.append(coordinates[i][1][0]+1)
                    first_l_coord.append(coordinates[i][0][1])
                    return True
    return False


#бинарная упаковка
def binary_packing(count):
    #процесс упаковки
    kol = 1
    while kol < count:
        #размеры текущего вписываемого прямоугольника
        current_w = WIDTHS[kol]
        current_l = LENGTHS[kol]
        #проход по большому прямоугольнику
        if (len(coordinates) == 0):
            coordinates.append([[0,0],[current_w-1,current_l-1]])
            first_w_coord.append(0)
            first_l_coord.append(0)
            kol += 1
        else:
            #поиск места
            if find_place(count, kol, current_w, current_l):
                kol += 1 
            else:
                #поиск свободного места при условии возможности поворота вписываемого прямоугольника
                if find_place(count, kol, current_l, current_w):
                    global fl_turn 
                    fl_turn = True
                    kol += 1 
                else:
                    return False
#            else:
#                return False        
    return True
                
        
#перестановка при сортировке
def permutation(i):
    WIDTHS[i],WIDTHS[i+1] = WIDTHS[i+1],WIDTHS[i]
    LENGTHS[i],LENGTHS[i+1] = LENGTHS[i+1],LENGTHS[i]
    SQUARES[i],SQUARES[i+1] = SQUARES[i+1],SQUARES[i]
    
#сортировка массивов    
def sort_arrays(count):
    n=1
    SQUARES.append(WIDTHS[0]*LENGTHS[0])
    #упорядочивание по площадям по убыванию
    while n < count:
        for i in range(count-n):
            SQUARES.append(WIDTHS[i+1]*LENGTHS[i+1])
            if WIDTHS[i]*LENGTHS[i] < WIDTHS[i+1]*LENGTHS[i+1]:
                permutation(i)
            #упорядочивание по ширине при одиноковых площадях
            elif (WIDTHS[i]*LENGTHS[i] == WIDTHS[i+1]*LENGTHS[i+1]):
                if (WIDTHS[i] < WIDTHS[i+1]):
                    permutation(i)
                #упорядочивание по длине при одиноковых площадях и ширине
                elif (WIDTHS[i] == WIDTHS[i+1]):
                    if (LENGTHS[i] < LENGTHS[i+1]):
                        permutation(i)
        n += 1

#проверка данных файла        
def check_for_errors(count):
    for i in range(count):
        if (WIDTHS[i]<1) or (LENGTHS[i]<1):
            return True
    return False

#чтение файла
def write_from_file():
  file = open('test2.txt', 'r') #файл для считывания параметров прямоугольников
  for line in file:
      row = [int(i) for i in line.split()]
      WIDTHS.append(row[0])
      LENGTHS.append(row[1])
  
# основная функция  
def main():
    t = time.clock()
    write_from_file()
    count = len(WIDTHS)
    if (check_for_errors(count)):
        print ('Значения параметров прямоугольников не являются натуральными числами')
    else:
        sort_arrays(count)
        #проверка на вместительность первого прямоугольника по площади
        sumSquare = 0
        for i in range(count):
            if i != 0:
                sumSquare += SQUARES[i]
        if (SQUARES[0] < sumSquare):
            print ("Задачи не имеют решений при данных параметрах прямоугольников")
        else:
            #упаковка прямоугольников
            if binary_packing(count):
                if fl_turn:
                    print("Задача имеет решение (c поворотом прямоугольников)")
                else:
                    print("Задача имеет решение (без поворотов прямоугольников)")
            else:
                print ("Задачи не имеют решений при данных параметрах прямоугольников")
    print( "Время выполнения алгоритма ", time.clock() - t )

      
if __name__=='__main__':
    main()
