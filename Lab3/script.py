
import module
#Меню для вибору відповідного завдання
while True:
    print("1. Task 1")
    print("2. Task 2")
    print("0. Exit")

    choice = int(input("Choose a task (0-2): "))

    if choice == 0:
        break
    elif choice == 1:
        module.Task1()
    elif choice == 2:
        module.Task2()
    else:
        print("Невірний вибір. Виберіть ще раз.")
        
        import module

module.Task1()