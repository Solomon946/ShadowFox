class Avenger: #Defining a class named Avenger
    def __init__(self, name, age, gender, super_power, weapon, leader=False): #Constructor to initialize the attributes of the class
        self.name = name #Instance variable for name
        self.age = age #Instance variable for age
        self.gender = gender #Instance variable for gender
        self.super_power = super_power #Instance variable for name of super power
        self.weapon = weapon #Instance variable for name of weapon
        self.leader = leader #Instance variable for leader status

    def get_info(self): #Method to display the information of avenger
        print("Name:", self.name) #printing the name of avenger
        print("Age:", self.age) #printing the age of avenger
        print("Gender:", self.gender) #printing the gender of avenger 
        print("Super Power:", self.super_power) #printing the super power of avenger 
        print("Weapon:", self.weapon) #printing the weapon of avenger 
        print() #printing a new line for better readability and formating 

    def is_leader(self): #This Method checks if the avenger is a leader or not
        if self.leader: #Checking if the leader attribute is True
            print(self.name, "is the leader of the Avengers\n") #Printing the avenger is the leader 
        else: #Using esle statement if the above condition is false
            print(self.name, "is not the leader of the Avengers\n") #printing the avenger is not the leader 


avengers = [ #Creating a list of avenger objects 
    Avenger("Captain America", 100, "Male", "Super Strength", "Shield", True), #Leader of avengers
    Avenger("Iron Man", 48, "Male", "Technology", "Armor"), #another avenger object
    Avenger("Black Widow", 35, "Female", "Superhuman", "Batons"), #another avenger object
    Avenger("Hulk", 40, "Male", "Unlimited Strength", "No Weapon"), #another avenger object
    Avenger("Thor", 1500, "Male", "Super Energy", "Mjölnir"), #another avenger object
    Avenger("Hawkeye", 38, "Male", "Fighting Skills", "Bow and Arrows") #another avenger object
]

for hero in avengers: #Iterating the list of avenger objects 
    hero.get_info() #Calling the get_info method for each avenger object to display their information
    hero.is_leader() #Calling the is_leader method for each avenger object to check if they are leader or not
