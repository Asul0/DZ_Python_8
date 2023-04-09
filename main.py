def show_all():
   file = open('sample.txt', 'r', encoding= 'UTF-8')
   data = file.readlines()
   file.close
   for i in data:
      print(i)
      
      
def add_contact ():
   file = open('sample.txt', 'a', encoding= 'UTF-8')
   data = input("Введите фамилию, телефон, коменнтарий, (разделляя ;)")
   data += '\n'
   file.write(data)
   file.close


def main_menu():
   print ("Main menu")
   print("1. Показать всю книгу")
   print("2. Добавить новую запись")
   print("3. Редактировать запись")
   print("4. Писк контакта")
   print("5. Go back to main menu")

def find_contact():
   find_string = input("Введите поисковой запрос: ")
   file = open('sample.txt', 'r', encoding= 'UTF-8')
   data = file.readlines()
   for index, data_str in enumerate(data):
      if find_string in data_str:
         print("found data =",data_str)


def edit_contact():
   find_string = input("Введите поисковой запрос: ")
   replace_string = input("Введите новые данные: ")
   file = open('sample.txt', 'r', encoding='UTF-8')
   data = file.readlines()
   data_new = []
   for data_str in data:
      if find_string in data_str:
            print("Найдена запись: ", data_str)
            data_new.append(replace_string + '\n')
      else:
            data_new.append(data_str)
   file.close()
   file = open('sample.txt', 'w', encoding='UTF-8')
   file.writelines(data_new)
   file.close()

def delete_contact():
   find_string = input("Введите поисковой запрос: ")
   file = open('sample.txt', 'r', encoding='UTF-8')
   data = file.readlines()
   data_new = []
   for data_str in data:
      if find_string not in data_str:
            data_new.append(data_str)
   file.close()
   file = open('sample.txt', 'w', encoding='UTF-8')
   file.writelines(data_new)
   file.close()

if __name__ == "__main__":
   main_menu()

   while True:
      choose =  int(input("Введите пункт меню: "))
      if choose == 1:
            show_all()
      if choose == 2:
            add_contact()
      if choose == 3:
            edit_contact()
      if choose == 4:
            find_contact()
      if choose == 5:
            delete_contact()
      if choose == 6:
            break
