WIDTHS = [] #массив ширины
LENGTHS = [] #массив длины
SQUARES = [] #площади прямоугольников
    
coordinates = []#лист для хранения координат
first_w_coord = []
first_l_coord = []


def check_busy_coordinates(current_first_coord, kol, current_w, current_l, k):
    coord_w = current_first_coord[0]
    coord_l = current_first_coord[1]
    #проверка на то, что точка является первой 
    #координатой вписанного прямоугольника
    if ((coord_w<WIDTHS[0] and coord_l<LENGTHS[0]) or
        (coord_w+current_w-1<WIDTHS[0] and coord_l+current_l-1<LENGTHS[0])):
        for i in range(kol-1):
            #проверка на совпадение с первой координатой
            if (coord_w == first_w_coord[i] and coord_l == first_l_coord[i]):
                return False
        #проверка на наложение на вписанные прямоугольники        
        for i in range(kol-1):
            if k == 1 and i==3:
                f_w = coord_w
                l_w = coord_w+current_w-1
                f_l = coord_l
                l_l = coord_l+current_l-1
                f_w_r = coordinates[i][0][0]
                l_w_r = coordinates[i][1][0]
                f_l_r = coordinates[i][0][1]
                l_l_r = coordinates[i][1][1]
            if (
#                (coord_w>=coordinates[i][0][0] and coord_w<=coordinates[i][1][0]) and 
#                (coord_l>=coordinates[i][0][1] and coord_l<=coordinates[i][1][1]) and
#                (coord_w+current_w-1>=coordinates[i][0][0] and coord_w+current_w<=coordinates[i][1][0]) and 
#                (coord_l+current_l>=coordinates[i][0][1] and coord_l+current_l<=coordinates[i][1][1])
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
    
def find_place(count, kol, current_w, current_l):
    for i in range(kol-1):
        current = [coordinates[i][0][0],coordinates[i][1][1]+1]
        k=0
        if kol ==5 and (current[0] == 4 and current[1] == 3):
            k=1
        
        #если справа есть свободное место или вписанных только один
        if (check_busy_coordinates(current, kol, current_w, current_l, k) or (kol == 1)):
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
        current = [coordinates[i][1][0]+1,coordinates[i][0][1]]        
        if (check_busy_coordinates(current, kol, current_w, current_l, k) or (kol == 1)):
            #если уместится по ширине и длине
            if ((WIDTHS[0]-coordinates[i][1][0]-1>=current_w) and
                ((LENGTHS[0]-coordinates[i][0][1]-1>=current_l) or
                 (LENGTHS[0]-coordinates[i][0][1]-1 == 0))):
#------------------------------------------------------------------------------
                #проверка на свободное место слева
#                check_current = [current[0], current[1]-1]
#                while(check_current[1]>=0):
#                    check_busy_coordinates(check_current, kol)
#                    check_current[1] -= 1
#------------------------------------------------------------------------------
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
                return False
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
  file = open('test_with_turn.txt', 'r') #файл для считывания параметров прямоугольников
  for line in file:
      row = [int(i) for i in line.split()]
      WIDTHS.append(row[0])
      LENGTHS.append(row[1])
  
# основная функция  
def main():
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
            fl = binary_packing(count)
            print (coordinates)
            if fl:
                print("Задача имеет решение (без поворотов прямоугольников)")
            else:
                print ("Задачи не имеют решений при данных параметрах прямоугольников")

      
if __name__=='__main__':
    main()
