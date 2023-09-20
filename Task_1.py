class SchoolJournal:
    def __init__(self, subject, student):
        self.subject = subject
        self.student = student
        self.grade_list = []
    def grade(self, n):
        self.grade_list.append(n)
    def printer(self):
        print(self.subject, self.student, self.grade_list)
    def final_grade(self):
        print(sum(self.grade_list)/len(self.grade_list))

SJ = SchoolJournal('Physics','Matre de Ebale')

from random import randint

for _ in range(15):
    SJ.grade(randint(2,100))

SJ.printer()
SJ.final_grade()