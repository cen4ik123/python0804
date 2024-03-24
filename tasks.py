import random


# def task1():
#    lists1 = list()
#    for i in range (10):
#        num1 = random.randrange(1,10)
#        lists1.append(num1)
#    print(lists1)
#    with open("test.txt", "w") as test_file:
#        for i in list1:
#            test_file.write(str(i))
#        for i in list1:
#            elem = random.choice(list1)
# task1()


# def task2():
#    list1 = list()
#    list2 = list()
#    for i in range (10):

# def task3():
#    print("выберите операцию")
#    print("1. посчитать")
#    print("2. записать")
#    print("3. посчитать")
#    operation = int(input("выберите операцию"))
#    if operation ==1:
#        print("1. посчитать площадь круга")
#        print("2. посчитать площадь прямоугольника")
#        print("3. посчитать площадь треугольника")
#        flag = "da"
#        while flag =="da":
#            num1 = str(input("введитте первую фигуру"))
#            if num1 == "круг":
#                pi = 3.14
#                r = int(input("введите радиус"))
#                s = pi * r ** 2
#                print(s)
#            elif num1 == "прямоугольник":
#                a = int(input("введите первую сторону"))
#                b = int(input("введите вторую сторону"))
#                s = a * b
#            elif num1 == "треугольник":
#                a = int(input("введите первую сторону"))
#                b = int(input("введите вторую сторону"))
#                с = int(input("введите третью сторону"))
#                p = a + b + c
#                s = math.sqrt(p * (p - a) * (p - b) * (p - c))
#                print(s)


# def task4():
#    new_list = list()
#    with open("test.txt", "r") as file1:
#        for line in file1:
#            if int(line) % 2 == 0:
#                new_list.append


# def task5():
#    movies = list()
#    while True:
#        movie = input("введите название фильма")
#        print("тобы закончить ввд введите 'stop' ")
#        if movie.lower() == 'stop':
#            break
#        else:
#            movies.append(movie)
#
#    with open("favourite_movies.txt", "w") as movies_file:
#        for movie in movies:
#            movies_file.write(movie + "\n")
#    for movie in movies:
#        print(movie)
# task5()


# def task6():
#    while True:
#        print("1. добавить новую задачу")
#        print("2. посмотреть список задач")
#        print("3. отметить задачу как выполненную")
#        print("4. удалить задачу")
#        print("5. выйи из программы")
#
#        choise = input("введите номер действия")
#
#        if choise == "1":
#            create_task_list()
#        elif choise == "2":
#            view_task_list()
#        elif choise == "3":
#            mark_task_done()
#        elif choise == "4":
#            delete_task()
#        elif choise == "5":
#            break
#        else:
#            print("некорректный ввод.попробуйте снова.")
#            def mark_task_done():
#                tasks = []
#                with open("tasks.txt", "r") as file:
#                    tasks = file.readlines()
#
#                print("список задач:")
#                for i,task in enumerate(tasks):
#                    print(f"{i + 1}. {task.trip()}")
#
#            while True:
#                print("выберите действие:")
#                print("1. добавить новую задачу")
#                print("2.посмотреть список задач")
# task6()


#            f
# def task7():
#    list1 = list()
#    rnum = random.randint(10,20)
#    for i in range (rnum):
#        list1.append(random.randint(0,100))
#    print(list1)
#    list1.sort()
#    print(list1)
#
# task7()


# def task21():
#
#
#
# data1 = ("hello, 12, 65.4, False, "hi")
# print(data1)
##data1[3] = True
# y


# def task13():
#     dict = {}
#     spisok = []
#     korteq = ()
#     sum1 = 0
#     sum2 = 0
#     i = "ключ"
#     for i in range(7):
#         key = input("ведите ключ ")
#         value = int(input("введите значение"))
#         dict[key] = value
#         if value %2 ==0:
#             sum1 +=value
#        else:
#            sum2+=value
#        if sum2 > sum1:
#            list.append(sum1)
#            list.append(sum2)
#            tuple = tuple(list)
#            list.clear()
#        else:
#            for value in dict.items()():
#                list.append(value)
#        print("список: ",list)
#        print("кортеж:", tuple)
#        print("словарь ",dict)

def task14():
    users = {}
    rnum = random.randint(0, 100)
    for i in range(3):
        key = input("ведите число")
        value = int(input("введите значение"))
        users[key] = value
        users.items()
        print(users)
        with open("numbers.txt", "a") as file:
            file.write(str(i) + "\n")


task14()
