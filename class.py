# [assignment] Skeleton class. Add your code here
from msilib.schema import SelfReg


def __init__(self, Name, age, tracks, score):
        self.Name = Name
        self.age = age
        self.tracks = tracks
        self.score = score
        
    #object of student
class Student:
    Name = "Bob"
    age = 34
    tracks = "full stack"
    score = 10.11
    print('class student: ')
    print('Name is a', Name)
    print('age is a', age)
    print('track is a', tracks)
    print('score is a', score)

    #class variables can be accessed using class
    #name also
    #print("\nAccessing class variable using class name")
    #print(SelfReg.name)

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
print("\nAccessing class variable using class name")
print(SelfReg.name)
