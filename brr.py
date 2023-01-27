
massiv = []
print ("Hello!")
print ("Введите количесто чисел")
kolvo = int(input("Количество = "))
print ("Отлично, а теперь нужно будет ввести сами числа!")
for i in range (kolvo):
    massiv.append(int(input("Введите число = ")))
 
print ("Введите знак + , - , /, * или **")
znak = input("Ваш знак это: ")
match znak:
    case '+':
        print ("OK")
        print ("Ответ = ", sum(massiv))
    case '*':
        proizvedenie = massiv [0]
        print ("OK")
        for i in range (1, len(massiv)):
            proizvedenie *=massiv[i] 
            
        print ("Ответ = ", proizvedenie)
            
    case '/':
        
        proizvedenie = massiv [0]
        print ("OK")
        for i in range (1, len(massiv)):
            if (massiv[i] == 0):
                print ("На ноль нельзя делить!")
                exit(0)
            else:
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
    