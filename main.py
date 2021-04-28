import random, time
import animal
from animal import Cat, Dog

def init_cat_dog():
    number_cat = random.randrange(1, 100)
    number_dog = 100 - number_cat
    list_cat = cat.add_cat(number_cat)
    list_dog = dog.add_dog(number_dog)
    animal.write_file(list_cat, list_dog)




def animal_eat(animal, count_animal):
    data_animal = []
    for i in range(count_animal):
        data_animal.append(i)
    number_animal_eaten = count_animal * 30 // 100
    while True:
        location = random.randrange(0, count_animal)
        if count_animal - len(data_animal) != number_animal_eaten:
            if location in data_animal:
                # data_animal.append(location)
                print(animal.eat(location))
                data_animal.remove(location)
        else:
            break
    return data_animal

    # data_animal[]


def dog_cat_eat():
    count_dog = len(data["Dog"])
    count_cat = len(data['Cat'])
    # animal_eat(cat, count_cat)
    # animal_eat(dog, count_dog)

    list_cat_not_eaten = animal_eat(cat, count_cat)
    list_dog_not_eaten = animal_eat(dog, count_dog)


    for n in list_cat_not_eaten:
        data["Cat"][n] -= 1

    for m in list_dog_not_eaten:
        data["Dog"][m] -= 2

    data_dog = data['Dog']
    data_cat = data['Cat']
    animal.write_file(data_cat, data_dog)



def run_pro1():
    number_feed = 6
    while number_feed > 0:
        print(number_feed)
        number_feed -= 1
        dog_cat_eat()
        time.sleep(10)


data = animal.read_file()
cat = Cat()
dog = Dog()


def show_dog_cat():
    name_cat = []
    name_dog = []
    for i in range(1, len(data['Cat'])+1):
        name_cat.append('cat' + str(i))

    for n in range(1, len(data['Dog'])+1):
        name_dog.append('dog' + str(n))

    list_cat = dict(zip(name_cat, data['Cat']))
    print("list cat: ", list_cat)

    list_dog = dict(zip(name_dog, data['Dog']))
    print("list dog: ", list_dog)


def dog_cat_fat():
    list_cat_fat = cat.statistics_cat('fat')
    list_dog_fat = dog.statistics_dog('fat')

    print('list of fat animals:')
    print('list cat:', list_cat_fat)
    print('list dog:', list_dog_fat)


def dog_cat_normal():
    list_cat = cat.statistics_cat('normal')
    list_dog = dog.statistics_dog('normal')

    print('list of normal animals:')
    print('list cat:', list_cat)
    print('list dog:', list_dog)


def dog_cat_dead():
    list_cat = cat.statistics_cat('dead')
    list_dog = dog.statistics_dog('dead')

    print('list of dead animals:')
    print('list cat:', list_cat)
    print('list dog:', list_dog)


def cat_fat():
    print(cat.statistics_cat('fat'))

def cat_normal():
    print(cat.statistics_cat('normal'))

def cat_dead():
    print(cat.statistics_cat('dead'))

def dog_fat():
    print(dog.statistics_dog('fat'))

def dog_normal():
    print(dog.statistics_dog('normal'))

def dog_dead():
    print(dog.statistics_dog('dead'))

def menu2():
    print("1: Thống kê số chó mèo.")
    print("2: Danh sách những con vật béo .")
    print("3: Danh sách những con bình thường")
    print("4: Danh sách những con đã chết")
    print("5: Danh sách những con mèo béo.")
    print("6: Danh sách những con mèo bình thường.")
    print("7: Danh sách những con mèo chết.")
    print("8: Danh sách những con chó béo.")
    print("9: Danh sách những con chó bình thường.")
    print("10: Danh sách những con chó chết.")

def run_funcion():
    x = int(input("Choose: "))
    switcher = {
        1: show_dog_cat,
        2: dog_cat_fat,
        3: dog_cat_normal,
        4: dog_cat_dead,
        5: cat_fat,
        6: cat_normal,
        7: cat_dead,
        8: dog_fat,
        9: dog_normal,
        10: dog_dead
    }
    if x not in switcher:
        raise Exception("not found")
    switcher[x]()

def repeat_menu():
    menu2()
    ctn = input("Enter 'Yes' to continue: ")
    while ctn == "Yes":
        menu2()
        run_funcion()
        ctn = input("Enter 'Yes' to continue: ")
    else:
        exit()


            #program 1
init_cat_dog()
run_pro1()


            #program 2
# repeat_menu()
