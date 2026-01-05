#Exercise 8
class Lecture:
    _nLectures=0
    def __init__(self, attendances):
        Lecture._nLectures +=1
        self._number= Lecture._nLectures
        self._attendances= attendances

    def __str__(self):
        return f"Lecture {self._number} with {self._attendances} attendances"

    @classmethod
    def resetClassNumber(cls):
        cls._nLectures=0

class RotativeClass(Lecture):
    def __init__(self, attendances, views):
        super().__init__(attendances)
        self._views= views

    def __str__(self):
        return f"{super().__str__()} and {self._views} views"



#main code
lectureAA= Lecture(80)
lectureOOP= RotativeClass(40, 30)
print(lectureAA)
print(lectureOOP)

print()
Lecture.resetClassNumber()
lectureMat=RotativeClass(50, 50)
print(lectureMat)

print()
Lecture.resetClassNumber()
lectures = [Lecture(i) for i in range(50,19,-3)]
for lecture in lectures:
    print(lecture)

print()
Lecture.resetClassNumber()
lg= [Lecture(i) for i in range(50,19,-3)]
lectures=list(lg)
for lecture in lectures:
    print(lecture)

print()
lectures.append(RotativeClass(20, 50))
lectures.append(RotativeClass(25, 30))
lectures.append(RotativeClass(22, 55))

for lecture in lectures:
    print(lecture)
