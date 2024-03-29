from abc import ABC, abstractmethod
import csv
from pprint import pprint 

#parent class
# class definition
class Cupcake(ABC):

    # attribute
    size = "regular"

    # instance attributes self refers to a specific obeject in memory
    # init method that is called when you initialize
    def __init__(self, name, price, flavor, frosting, filling):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []

    # instance method
    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)

  # decorator 
    @abstractmethod
    def calculate_price(self, quantity):
        return quantity * self.price
    
    #child class
class Mini(Cupcake):

    size = "mini"

    # Filling is overwritten is by child class
    # instance attributes of a instance mini cupcake
    def __init__(self, name, price, flavor, frosting):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []

    #instance method
    def calculate_price(self, quantity):
        if quantity > 12:
             new_price = self.price * .5
        else: 
             new_price = self.price

        return new_price * quantity
    
    #child class
    # class definition
class Regular(Cupcake):
    
    size = "regular"
# INHERITS INSTANCE ATTRIBUTES AND METHODS BUT NOT ABSTRACT METHOD
    def calculate_price(self, quantity):
        return quantity * self.price
        

    #child class
class Large(Cupcake):
    size = "large"
        # INHERITS INSTANCE ATTRIBUTES AND METHODS BUT NOT ABSTRACT METHOD
    def calculate_price(self, quantity):
        return quantity * self.price
    
### Cupcake instances that we are instantiating or initialinzing
cupcake1 = Mini("Oreo", 1.00, "Chocolate", "Cookies and Cream")
cupcake2 = Regular("Oreo", 2.00, "Chocolate", "Cookies and Cream", None)
cupcake3 = Large("Red Velvet", 3.00, "Red Velvet", "Cream Cheese", None)

# Condensing instances into a list 
cupcake_list = [cupcake1, cupcake2, cupcake3]

### Functions to add cupcake classes to file

def write_new_csv(file, cupcakes):
    with open(file,"w", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for cupcake in cupcakes:
            if hasattr(cupcake, "filling"):
                writer.writerow({
                    "size": cupcake.size,
                    "name": cupcake.name,
                    "price": cupcake.price,
                    "flavor": cupcake.flavor,
                    "frosting": cupcake.frosting,
                    "sprinkles": cupcake.sprinkles,
                    "filling": cupcake.filling
                })
            else:
                writer.writerow({
                    "size": cupcake.size,
                    "name": cupcake.name,
                    "price": cupcake.price,
                    "flavor": cupcake.flavor,
                    "frosting": cupcake.frosting,
                    "sprinkles": cupcake.sprinkles,
                })
 # defining fuction as add cupcake
def add_cupcake(file, cupcake):
    # opening up in a mode which will append to the csvfile. \n each new line has the character.
    with open(file, "a", newline="\n") as csvfile:
        
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if hasattr(cupcake, "filling"):
            writer.writerow({
                "size": cupcake.size, 
                "name": cupcake.name, 
                "price": cupcake.price, 
                "flavor": cupcake.flavor, 
                "frosting": cupcake.frosting, 
                "filling": cupcake.filling, 
                "sprinkles": cupcake.sprinkles})
        else:
            writer.writerow({
                "size": cupcake.size, 
                "name": cupcake.name, 
                "price": cupcake.price, 
                "flavor": cupcake.flavor, 
                "frosting": cupcake.frosting, 
                "sprinkles": cupcake.sprinkles
            })



### Functions to add the cupcake dictionaries to file
def get_cupcakes(file):
    with open(file, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        reader = list(reader)
        return reader
    
def find_cupcake(file, name):
    for cupcake in get_cupcakes(file):
        if cupcake["name"] == name:
            return cupcake
    return None

def add_cupcake_dictionary(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
       
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(cupcake)


def read_csv(csvfile):
    with open("file") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            pprint(row)

