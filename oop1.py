#position,name,age,level,salary
se1=['Software Engineer','Stefan',20,'Junior',5000]
se2=['Software Engineer','Lisa',25,'Senior',7000]



#class

class SoftwareEngineer:
    # class attribute
    alias = "keyboard magician"

    def __init__(self,name,age,level,salary):
        # instance attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary





# instance
se1=SoftwareEngineer('Stefan',20,'Junior',5000)
print (se1.name,se1.age)
print(SoftwareEngineer.alias)
se2 = SoftwareEngineer('Lisa',25,'Senior',7000)
print (se2.alias)

