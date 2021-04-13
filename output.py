class passenger:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
    
    def __str__(self):
        return f'{self.name} - {self.capacity}'

class cargo:
    def __init__(self, name, weight_limit):
        self.name = name
        self.weight_limit = weight_limit
    
    def __str__(self):
        return f'{self.name} - {self.weight_limit}'

def greet(greeting):
    ticket = input("Do you have a ticket? ")
    if ticket == "yes":
        print(greeting)
    elif ticket == "no":
        print("Sorry, looks like you don't have a ticket!")

greet("Welcome aboard passenger!")