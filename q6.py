"""
Create 2 different classes Major and Subject
create an instance of Major and add different subjects to the 'subject' attribute as a set of subjects
Create another instance for Major and add subjects to the instance
add operator overloading to add different methods so that we can create another major.
Example we have majors science, commerce
if we call
new_major = science + commerce
it should be able to return the new instance of Major with all subjects inside of them
Note:
    you can try other operator overloading options too.
"""
class Subject:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Subject:{self.name}"

    def __repr__(self):
        return self.__str__()


class Major:
    name = ''

    def __init__(self, name):
        self.name = name
        self.subjects = []

    def __add__(self, other: "Major"):
        sub = Major(f"{self.name} + {other.name}")
        sub.subjects = [*self.subjects, *other.subjects]
        return sub
s1 = Major("Science")
s1.subjects.append(Subject('Physics'))
s1.subjects.append(Subject('Chemistry'))

c1 = Major("Commerce")
c1.subjects.append(Subject('Business Mathematics'))
c1.subjects.append(Subject('Accounting'))

new_major = s1+ c1

print(new_major.name)
print(new_major.subjects)