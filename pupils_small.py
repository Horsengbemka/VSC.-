class Pupil:
    def __init__(self, surname, name, mark):
        self.surname = surname
        self.name = name 
        self.mark = mark

pupils = []

def print_class(pupils):
    for pupil in pupils:
        print(pupil.surname, pupil.name, "-", pupil.mark)
    print("\n")

def print_five(pupils):
    print("Відмінники:")
    for pupil in pupils:
        if pupil.mark == 5:
            print(pupil.surname)
    print("\n")

def

with open

print_class()
print_five()