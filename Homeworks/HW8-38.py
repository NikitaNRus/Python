# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле. 
# 1.Программа должна выводить данные 
# 2.Программа должна сохранять данные в текстовом файле 
# 3.Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека) 
# 4.Использование функций. Ваша программа не должна быть линейной

def Ending():
    ending = input("Закончить программу? - напечатай 'yes' или 'no':\n")
    ending.lower()
    if ending == 'no':
        on = 1
    elif ending == 'yes':
        on = 0
    else: 
        print("Неверное значение: напечатай 'yes' или 'no': \n")
        Ending()
    return(on)

def ReadBook(file):
    print('ПРОСМОТР СПРАВОЧНИКА')
    with open (file, 'r+', encoding='utf-8') as f:
        print(f.readlines())
    

def InputData(file):
    print('ВНЕСЕНИЕ ДАННЫХ')
    name = (input('Введите имя: '))
    familyname = (input('Введите фамилию: '))
    lastname = (input('Введите отчество: '))
    phone = (input('Введите номер телефона: '))
    list = [name, familyname, lastname, phone]
    with open (file, 'r+', encoding='utf-8') as f:
        text = f.readlines()
        n=0
        for line in text:
            n+=1
            if name in line and familyname in line:
                print('Такое имя есть в справочнике!')
                a = input('Хотите внести его повторно? введите "да" или "нет": \n')
                if a =='нет': break
        f.write('\n')
        for line in list:
            f.writelines(line +' ') 
        print('ФИО и телефон успешно внесены в справочник!')
    

def SearchData(file):
    print('ПОИСК ДАННЫХ')
    name = (input('Введите имя: '))
    familyname = (input('Введите фамилию: '))
    n = 0
    with open (file, 'r+', encoding='utf-8') as f:
        text = f.readlines()
        for line in text:
            n+=1
            if name in line and familyname in line:
                print(line, 'найдено в строчке', n )

    

def EditData(file):
    print('РЕДАКТИРОВАНИЕ ДАННЫХ')
    name = (input('Введите имя, которое хотите найти: '))
    familyname = (input('Введите фамилию, которую хотите найти: '))
    n = 0
    list = []
    with open (file, 'r+', encoding='utf-8') as f:
        for line in f:
            n+=1
            if name in line and familyname in line:
                print(line, 'найдено в строчке', n )
                list.append(n)
        edit = int(input('Введите номер строчки для редактирования: \n'))
    with open (file, 'r+', encoding='utf-8') as f:    
        n = 0
        text = f.readlines()
        newtext = []
        for line in text:
            n+=1
            if n !=edit:
                newtext.append(line)
            if n == edit:
                list = line.split(' ')
                list[3] = input('Введите новый номер телефона: ')
                st = ''
                for i in list:
                    st +=str(i)+" "
                st+='\n'
                newtext.append(st)
        print(newtext)
    with open (file, 'w', encoding='utf-8') as f: 
        for i in newtext:
            f.writelines(i)
            print(i) 
    print('Телефон успешно перезаписан!')   


def DeleteData(file):
    print('УДАЛЕНИЕ ДАННЫХ')
    name = (input('Введите имя, которое хотите найти: '))
    familyname = (input('Введите фамилию, которую хотите найти: '))
    n = 0
    list = []
    with open (file, 'r+', encoding='utf-8') as f:
        for line in f:
            n+=1
            if name in line and familyname in line:
                print(line, 'найдено в строчке', n )
                list.append(n)
        edit = int(input('Введите номер строчки для удаления: \n'))
    with open (file, 'r+', encoding='utf-8') as f:    
        n = 0
        text = f.readlines()
        newtext = []
        for line in text:
            n+=1
            if n !=edit:
                newtext.append(line)
    with open (file, 'w', encoding='utf-8') as f: 
        for i in newtext:
            f.writelines(i)
            print(i) 
    print('ФИО и телефон успешно удалены!') 


on = 1
file = 'PhoneBook.txt'
while on == 1:
    print('1 - Посмотреть весь телефонный справочник \n 2 - Найти запись в справочнике по фамилии и имени \n 3 - Внести новую запись в справочник \n 4 - Удалить запись из справочника \n 5 - Изменить телефон в справочнике \n ')
    
    action = int(input('Выберите действие: '))
    if action ==1:
        ReadBook(file)
        
    elif action == 2:
        SearchData(file)
        
    elif action == 3:
        InputData(file)

    elif action == 4:
        DeleteData(file)

    elif action == 5:
        EditData(file)

    on = Ending()
    if on==0: print('Конец программы')

    

    
