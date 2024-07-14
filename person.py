"""File for creating Person objects"""

class Person:
    """Defines a Person class, suitable for use in a hospital context.
    Data attributes: name of type str
                     age of type int
                     weight (kg) of type float
                     height (metres) of type float
    Methods: bmi()
             status()
    """

    def __init__(self, name, age, weight, height):
        """Creates a new Person object with a specified name, age, weight, and
        height."""

        self.name = name
        self.age = age
        self.weight = weight
        self.height = height


    def bmi(self):
        """Returns the body mass index of the person"""
        return self.weight / (self.height * self.height)

    def status(self):

        if self.bmi() < 18.5:
            return "Underweight"
        if self.bmi() >= 18.5 and self.bmi() < 25:
            return "Normal"
        if self.bmi() >= 25 and self.bmi() < 30:
            return "Overweight"
        if self.bmi() >= 30:
            return "Obese"


    def __str__(self):
        """Returns the formatted string represent of the Person object"""
        name = self.name
        age = self.age
        bmi = self.bmi()
        status = self.status()
        template = "{0} ({1}) has a bmi of {2:3.2f}. Their status is {3}."
        return template.format(name, age, bmi, status)    



def read_people(csv_filename):
    persons = []  # list for Person objects

    with open(csv_filename, "r") as file:  
        for line in file:
            args = line.split(",")

            for i in range(1, len(args)):  # convert arguments to float
                args[i] = float(args[i])

            persons.append(Person(*args))  # add Person objects to list
    return persons




bods = read_people("people1.csv")
for bod in bods:
    print(bod)
    print()