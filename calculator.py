
#print ("Выберите действие (необходимо выбрать номер):")
#print ("1) Авторизация ")
#print ("2) Регистрация")
#vibor = input("Ваш выбор = ")

#if (vibor == '1'):
    #login = input("Введите логин = ")
    

        


massiv = []
print ("Hello!")
print ("Введите количесто чисел")
print ("Введите знак операции, которую вы хотите провернуть")
znak = input("Ваш знак это: ")
match znak:
    case '+':
        print ("Введите количесто чисел")
        kolvo = int(input("Количество = "))
        print ("Отлично, а теперь нужно будет ввести сами числа!")
        for i in range (kolvo):
            massiv.append(int(input("Введите число = ")))
 
        print ("OK")
        print ("Ответ = ", sum(massiv))
    case '*':
        print ("Введите количесто чисел")
        kolvo = int(input("Количество = "))
        print ("Отлично, а теперь нужно будет ввести сами числа!")
        for i in range (kolvo):
            massiv.append(int(input("Введите число = ")))
        proizvedenie = massiv [0]
        print ("OK")
        for i in range (1, len(massiv)):
            proizvedenie *=massiv[i] 
            
        print ("Ответ = ", proizvedenie)
            
    case '/':
        print ("Введите количесто чисел")
        kolvo = int(input("Количество = "))
        print ("Отлично, а теперь нужно будет ввести сами числа!")
        for i in range (kolvo):
            chislo = int (input ("Введите число "))
            if (chislo == 0):
                print ("В операции деления не может быть 0! Включена инструкция по агрессивной замене!")
                chislo = 1
                massiv.append (chislo)
            else:
                massiv.append (chislo)
                   
                   
        proizvedenie = massiv [0]
        print ("OK")
        
        for i in range (1, len(massiv)):
            proizvedenie /=massiv[i] 
        print ("Ответ = ", proizvedenie)
        
    case '-':
        proizvedenie = massiv [0]
        print ("OK")
        for i in range (1, len(massiv)):
            proizvedenie -=massiv[i] 
        print ("Ответ = ", proizvedenie)
        
    case "**":
         if (len(massiv) > 2):
            print ("Для степени нужно лишь 2 числа!")
             
         else:
            print ("OK")
            print ("Ответ: ", massiv[0] ** massiv[1]) 
    
    
    