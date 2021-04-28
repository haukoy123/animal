from datetime import datetime
import pickle, pprint, random, time

class Animal:
    weight = 0
    def __init__(self):
        pass
    def bark(self, call):
        return call

    def eat(self, class_name, weight_gain, weight_max, weight_min, location):
        if self.weight <= weight_min:
            return f"I'm a {class_name} and I'm so dead!"
        else:
            self.weight = data[class_name][location]
            self.weight += weight_gain
            data[class_name][location] = self.weight
            if self.weight >= weight_max:
                return f"Mlom mlom! I'm a fat {class_name} with weight {self.weight}, {self.bark()}"
            else:
                return f"Mlem mlem! I'm a {class_name} with weight {self.weight}, {self.bark()}"

    def add_cat_dog(self, weight, number ):
        data_cat_dog = []
        for i in range(number):
            data_cat_dog.append(weight)
        return data_cat_dog

class Dog(Animal):
    def __init__(self):
        self.weight = 20
    def bark(self):
        call = "meow meow meow"
        return super(Dog, self).bark(call)
    def eat(self, location):
        weight_gain = 5
        weight_max = 30
        weight_min = 16
        return super(Dog, self).eat(self.__class__.__name__,
                                    weight_gain, weight_max, weight_min, location)
    def add_dog(self,number):
        return super(Dog, self).add_cat_dog(self.weight, number)

    def statistics_dog(self, key_word):
        name_dog = []
        data_dog = []
        if key_word =="fat":
            for n in range(len(data['Dog'])):
                if data['Dog'][n] >= 30:
                    name_dog.append('dog' + str(n + 1))
                    data_dog.append(data['Dog'][n])
        elif key_word == "dead":
            for n in range(len(data['Dog'])):
                if data['Dog'][n] <= 16:
                    name_dog.append('dog' + str(n + 1))
                    data_dog.append(data['Dog'][n])
        else:
            for n in range(len(data['Dog'])):
                if data['Dog'][n] <30 and data['Dog'][n] > 16:
                    name_dog.append('dog' + str(n + 1))
                    data_dog.append(data['Dog'][n])

        return dict(zip(name_dog, data_dog))



class Cat(Animal):

    def __init__(self):
        self.weight = 10
    def bark(self):
        call = "woof woof woof"
        return super(Cat, self).bark(call)
    def eat(self, location):

        weight_gain = 2
        weight_max = 13
        weight_min = 8
        return super(Cat, self).eat(self.__class__.__name__,
                                    weight_gain, weight_max, weight_min, location)

    def add_cat(self, number):
        return super(Cat, self).add_cat_dog(self.weight, number)

    def statistics_cat(self, key_word):
        name_cat = []
        data_cat = []
        if key_word =="fat":
            for i in range(len(data['Cat'])):
                if data['Cat'][i] >= 13:
                    name_cat.append('cat' + str(i + 1))
                    data_cat.append(data['Cat'][i])
        elif key_word == "dead":
            for i in range(len(data['Cat'])):
                if data['Cat'][i] <= 8:
                    name_cat.append('cat' + str(i + 1))
                    data_cat.append(data['Cat'][i])
        else:
            for i in range(len(data['Cat'])):
                if data['Cat'][i] > 8 and data['Cat'][i] < 13:
                    name_cat.append('cat' + str(i + 1))
                    data_cat.append(data['Cat'][i])

        return dict(zip(name_cat, data_cat))


data = {}
def write_file(cat, dog):
    data["Dog"] = dog
    data['Cat'] = cat
    output = open('animal.dat', 'wb')
    pickle.dump(data, output)
    output.close()


def read_file():
    global data
    pkl_file = open('animal.dat', 'rb')
    data = pickle.load(pkl_file)
    pkl_file.close()
    return data

def init_cat_dog():
    cat = Cat()
    dog = Dog()
    number_cat = random.randrange(1, 100)
    number_dog = 100 - number_cat
    list_cat = cat.add_cat(number_cat)
    list_dog = dog.add_dog(number_dog)
    write_file(list_cat, list_dog)
    # print(number_cat, number_dog)

cat = Cat()
dog = Dog()


def animal_eat(animal, count_animal):
    data_animal = []
    number_animal_eaten = count_animal * 30 // 100
    while True:
        a = random.randrange(0, count_animal)
        if len(data_animal) != number_animal_eaten:
            if a not in data_animal:
                data_animal.append(a)
                print(animal.eat(a))
        else:
            break


def dog_cat_eat():
    count_dog = len(data["Dog"])
    count_cat = len(data['Cat'])
    animal_eat(cat, count_cat)
    animal_eat(dog, count_dog)

    print(data)
    data_dog = data['Dog']
    data_cat = data['Cat']
    write_file(data_cat, data_dog)


