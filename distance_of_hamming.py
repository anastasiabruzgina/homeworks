import codecs, time, os

def distance_of_hamming(standard:str, string:str) -> int:
    distance = 0
    for i in range(len(standard)):
        if standard[i] != string[i]:
            distance += 1
    return distance

if __name__ == '__main__':
    a = input('''Добро пожаловать! Это программа сортирует строки файла по возрастанию расстояния Хэмминга. Программа запросит у вас файл со строками для сортировки и саму эталонную строку. Чтобы продолжить работу программы, нажмите Enter. Чтобы выйти, напишите "exit" \n''')

    while True:
        if a == 'exit':
            print('До новых встреч!')
            time.sleep(2)
            break
    
        standard = str(input('Эталонная строка:\n'))
        len_string = len(standard)
        output_file = str(input('Введите путь к файлу со строками: \n'))
        dict_of_distance = {}
        
        with codecs.open(output_file, "r", "utf_8_sig") as file:
            strings = [current_place.rstrip() for current_place in file.readlines()]
            for i in strings:
                if len(i) == len_string:
                    dict_of_distance[i] = distance_of_hamming(standard, i)
                    
            sorted_distance = sorted(dict_of_distance.items(), key = lambda item: item[1])
            
            i = 0
            result = []
            while i < len(sorted_distance):
                result.append(sorted_distance[i][0])            
                i += 1 
            print('\n')
            print('Результат выполнения программы находится в файле output.txt')
            print('\n')
            
            with open('output.txt', 'w') as result1:
                for i in result:
                    result1.write(i)
                    result1.write('\n')
            os.startfile('output.txt')
            
        b = str(input('Для выхода напишите "exit", для продолжения нажмите Enter\n'))
        print('\n')
        print('\n')
        if b == 'exit':
            print('До новых встреч!')
            time.sleep(2)
            break
        
    
