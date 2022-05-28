# [assignment] Skeleton class. Add your code here
from msilib.schema import SelfReg


def __init__(self, Name, age, tracks, score):
        self.Name = Name
        self.age = age
        self.tracks = tracks
        self.score = score
    #create the first object
    #object of student
class Student:
    Name = "Bob"
    age = 34
    tracks = "UI/UX"
    score = 10.11
    print('class student: ')
    print('Name is a', Name)
    print('age is a', age)
    print('track is a', tracks)
    print('score is a', score)

print("\nAccessing class variable using class name")
print(SelfReg.name)
