from django.db import models

numbers = []
for i in range(1,51):
    j = (str(i),str(i))
    numbers.append(j)

QUESTION_CHOICE=tuple(numbers)



YEAR_CHOICES = (
    ("2011","2011"),
    ("2012","2012"),
    ("2015","2015"),
    ("2016","2016"),
    ("2017","2017"),
    ("2018","2018"),
    ("2019","2019"),
    ("2020","2020"),
)

ANSWER_CHOICES = (
    ("1","1"),
    ("2","2"),
    ("3","3"),
    ("4","4"),
    ("5","5")
)

LESSON_CHOCIES = (
("unit","unit"),
("mechanics ","mechanics"),
("waves","waves"),
("optics","optics"),
("heat","heat"),
("gravity","gravity"),
("electro","electro"),
("magnetic","magnetic"),
("current","current"),
("elctronics ","electronic"),
("propertise of matter","propertise of matter"),
("heat wave","heat wave")
)
class Wiwarana(models.Model):
    year = models.CharField(max_length=4,choices=YEAR_CHOICES)
    lesson = models.CharField(max_length=500,choices=LESSON_CHOCIES,blank=True,null=True)
    number = models.CharField(max_length=2,choices=QUESTION_CHOICE,blank=True,null=True)
    note = models.TextField()
    answer = models.CharField(max_length=1,choices=ANSWER_CHOICES)