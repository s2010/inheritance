class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color
    def show_info(self):
        print("Last name :"+self.last_name)
        print("Eye color :"+self.eye_color)

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor Called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys
    def show_info(self):
        print("Last name :"+self.last_name)
        print("Eye color :"+self.eye_color)
        print("Number of Toys :" + str(self.number_of_toys))
        
bashayer = Child("Hijji", "Brown", 3)

#print(bashayer.last_name)
#print(bashayer.number_of_toys)

bashayer.show_info()
