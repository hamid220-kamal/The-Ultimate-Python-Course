class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000

    def __init__(self, name, salary, language): # dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")
 
 
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")


Hamid = Employee("Hamid", 1300000, "JavaScript") 
# Hamid.name = "Hamid"
print(Hamid.name, Hamid.salary, Hamid.language)

rohan = Employee()