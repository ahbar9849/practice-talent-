class student :
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_name(self,mesaage):
        print(self.name,mesaage)
s1 = student("ahbar",22,"A")
s2 = student("ahbar",22,"A")
s3 = student("ahbar",22,"A")
print(s1.name)

s1.get_name("aur kaise hai mama")