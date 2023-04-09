# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи (Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

# file = open('Contacts.txt', 'r', encoding='UTF-8')
# data = file.readlines()
# print(data)
# file.close()

print('Телефонный справочник')
print('1. Показать всю книгу')
print('2. Добавить номер')
print('3. Удалить контакт')
print('4. Редактировать контакт')
print('5. Поиск контакта')
choose = int(input('Выберите действие: '))

if choose == 1:
    def show_all():
        file = open('Contacts.txt', 'r', encoding='UTF-8')
        data = file.readlines()
        file.close()
        return data
    D = show_all()
    for i in D:
        print(i)

if choose == 2:
    def add_contact():
        add_string = input('Введите данные контакта (ФИО; тел; описание): ')
        file = open('Contacts.txt', 'a', encoding='UTF-8')
        file.write('\n')
        file.write(add_string)
        file.close() 
    add_contact() 

if choose == 3:
    def del_contact():
        del_string = input('Введите удаляемый контакт: ')
        file = open('Contacts.txt', 'r', encoding='UTF-8')
        data = file.readlines()
        file.close()

        file = open('Contacts.txt', 'w', encoding='UTF-8')
        for data_string in data:
            if del_string in data_string:
                print()
            else:
                file.write(data_string)
        file.close()
    del_contact()  

if choose == 4:
    def repl_contact():
        repl_string = input('Введите изменяемый контакт: ')
        var_contact = input('Введите на что нужно поменять (ФИО; тел; прим): ')
        file = open('Contacts.txt', 'r', encoding='UTF-8')
        data = file.readlines()
        file.close()

        file = open('Contacts.txt', 'w', encoding='UTF-8')
        for data_string in data:
            if repl_string in data_string:
                file.write(var_contact)
                file.write('\n')                
            else:
                file.write(data_string)
        file.close()
    repl_contact()       

if choose == 5:
    def find_contact():
        find_string = input('Введите поисковый запрос: ')
        file = open('Contacts.txt', 'r', encoding='UTF-8')
        data = file.readlines()
        for data_string in data:
            if find_string in data_string:
                print('Искомый контакт = ', data_string)
        file.close()
    find_contact()
