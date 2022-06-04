class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self, name):
        print("My new name is", name)

    def change_age(self, age):
        print("My age has changed to", age)

    def add_track(self, track):
        print("I have changed my track to", track)

    def get_score(self):
        print("I scored", self.score)


Bob = Student("Bob", 26, ["FE", "BE"], 20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()