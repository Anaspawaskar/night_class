class Animal:
    def __init__(self,legs, hands, eating_type, habitat_type):
        self.legs = legs
        self.hands = hands 
        self.eating_type = eating_type
        self.habitat_type = habitat_type

class Monkey(Animal):
    def __init__(self, legs, hands, eating_type, habitat_type):
        super().__init__(legs, hands, eating_type, habitat_type)
    
    def monkey(self):
        print("monkey chatters")
        self.key_value()
    
    def key_value(self):
        print("attributes of monkey :")
        for key, values in self.__dict__.items():
            print(f"{key}:{values}") 

monkey_object = Monkey(legs = 2, hands = 2, eating_type = "omnivorse", habitat_type = "Land")
# monkey_object.monkey()

class Cow(Animal):

    def __init__(self, legs, hands, eating_type, habitat_type):
        super().__init__(legs, hands, eating_type, habitat_type)

    def cow(self):
        print("cow says moooooooo")
        print(self.key_value())

    def key_value(self):
        print("attributes of Cow :")
        for key, values in self.__dict__.items():
            print(f"{key}:{values}")     

cow_object = Cow(legs = 4, hands = 0, eating_type = "omnivorse", habitat_type = "Land")
# cow_object.cow()


class Dog(Animal):
    def __init__(self, legs, hands, eating_type, habitat_type):
        super().__init__(legs, hands, eating_type, habitat_type)

    def dog(self):
        print("dog barks")
        return (self.key_value())
        
    def key_value(self):
        print("attributes of Dog :")
        for key, values in self.__dict__.items():
            print(f"{key}:{values}") 


dog_object = Dog(legs = 4, hands = 0, eating_type = "omnivorse", habitat_type = "Land")
# dog_object.dog()


class Cat(Animal):
    def __init__(self, legs, hands, eating_type, habitat_type):
        super().__init__(legs, hands, eating_type, habitat_type)
    
    def cat(self):
        print("cat says meow meow")
        self.key_value

    def key_value(self):
        print("attributes of cat :")
        for key, values in self.__dict__.items():
            print(f"{key}:{values}") 


cat_object = Cat(legs = 4, hands = 0, eating_type = "omnivorse", habitat_type = "Land")
# cat_object.cat()


class Crow(Animal):
    def __init__(self, legs, hands, eating_type, habitat_type):
        super().__init__(legs, hands, eating_type, habitat_type)


    def crow(self):
        print("crow says caow caow")
        self.key_value

    def key_value(self):
        print("attributes of Crow :")
        for key, values in self.__dict__.items():
            print(f"{key}:{values}") 

crow_object = Crow(legs = 2, hands = 2, eating_type = "omnivorse", habitat_type = "omnivorse")
# crow_object.dog()

class Donkey(Animal):
    def __init__(self, legs, hands, eating_type, habitat_type):
        super().__init__(legs, hands, eating_type, habitat_type)


    def donkey(self):
        print("cat says dhichu dhichu")
        self.key_value

    def key_value(self):
        print("attributes of donkey :")
        for key, values in self.__dict__.items():
            print(f"{key}:{values}") 


donkey_object = Donkey(legs = 4, hands = 0, eating_type = "omnivorse", habitat_type = "Land")
# donkey_object.donkey()

class Horse(Animal):
    def __init__(self, legs, hands, eating_type, habitat_type):
        super().__init__(legs, hands, eating_type, habitat_type)


    def horse(self):
        print("horse says neigh")
        self.key_value

    def key_value(self):
        print("attributes of horse :")
        for key, values in self.__dict__.items():
            print(f"{key}:{values}") 


Horse_object = Horse(legs = 4, hands = 0, eating_type = "omnivorse", habitat_type = "Land")
# donkey_object.donkey()


class Goat(Animal):
    def __init__(self, legs, hands, eating_type, habitat_type):
        super().__init__(legs, hands, eating_type, habitat_type)


    def goat(self):
        print("goat says baaa")
        self.key_value

    def key_value(self):
        print("attributes of goat :")
        for key, values in self.__dict__.items():
            print(f"{key}:{values}") 


goat_object = Goat(legs = 4, hands = 0, eating_type = "omnivorse", habitat_type = "Land")



class Sheep(Animal):
    def __init__(self, legs, hands, eating_type, habitat_type):
        super().__init__(legs, hands, eating_type, habitat_type)


    def sheep(self):
        print("sheep says baa")
        self.key_value

    def key_value(self):
        print("attributes of sheep :")
        for key, values in self.__dict__.items():
            print(f"{key}:{values}") 


sheep_object = Sheep(legs = 4, hands = 0, eating_type = "omnivorse", habitat_type = "Land")

        

while True:
    choice = input("choose the animals you wanna listen what they says :")
    if choice == "a":
        monkey_object.monkey(),"\n\n",cow_object.cow(),"\n\n",dog_object.dog()
    elif choice == "b":
        cat_object.cat(),crow_object.dog(),donkey_object.donkey()
    elif choice == "c":
        donkey_object.donkey(),goat_object.goat(),sheep_object.sheep()





        
        




    elif choice == "d":
        print("thank you for coming here ")
        break






































# while True:
#     user_choice = input("choose any one of the to know how does the animals sounds (a,b,c) :")
#     if user_choice == "a":
#         Self.Monkey()






















































    



