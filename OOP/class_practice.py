# I created a class containing two methods one that calculates average and second prints out reults based on the average

class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def average(self):
        result = sum(self.scores) / len(self.scores)
        return result

    def check_result(self):
        avg = self.average()
        if avg >= 70:
            print('Excellent')
        elif avg < 70 and avg >= 50:
            print('passed')   
        else:
            print('Failed') 
                 
        
    

student1 = Student('Marcel', [70, 80, 90])
student2 = Student("David", [40, 50, 45])
student3 = Student("Sarah", [55, 60, 65])
# print(student1.average()) 
student1.check_result()
student2.check_result()
student3.check_result()

# i created a class that loops through passed subjects by counting them.
# The second method loops through the parameter scores and appends scores less than 50 to a list to display failed scores.
class Subject:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def count_passed_subjects(self):
        counter = 0
        for score in self.scores:
            if score >= 50:
                counter = counter + 1
        print(counter)

    def get_failed_subjects(self):
        failed_Score = []
        for score in self.scores:
            if score < 50:
                failed_Score.append(score)
        return failed_Score

student1 = Subject("Marcel", [70, 40, 90, 30, 80])

student1.count_passed_subjects()
print(student1.get_failed_subjects())



# Create a method called get_grade() that checks each student's score and returns a list of grades.
# Score	          Grade
# 70 and above  	A
# 60–69	            B
# 50–59	            C
# Below 50	        F
class Grading:
    def __init__(self, name, grade_score):
        self.name = name
        self.grade_score = grade_score

    def get_grade(self):
        grades = []
        for grade in self.grade_score:
            if grade >= 70:
                grades.append('A') 
            elif grade >= 60:
                grades.append('B')
            elif grade <= 59 and grade >= 50:
                grades.append('C')
            else:
                grades.append('F')
        return grades


student1 = Grading('Marcel', [75, 45, 65, 55, 90])
print(student1.get_grade())


#Using Dictionaries in class
class School:
    def __init__(self, students):
        self.students = students

    def show_passed_students(self):
        passed = []
        for i in self.students:
            if i['score'] >= 50:
                passed.append(i['name'])
        return passed

students = [
    {"name": "Marcel", "score": 75},
    {"name": "David", "score": 45},
    {"name": "Sarah", "score": 85},
    {"name": "Mike", "score": 30},
    {"name": "Grace", "score": 60}
] 

school = School(students)
print(school.show_passed_students())

# Updating Dictionaries inside class methods

class Update:
    def __init__(self, students):
        self.students = students

    def update_score(self, name, new_score): 
        for u in self.students:
            if u['name'] == name:
                u['score'] = new_score
                print('Name Found!') 
                print(u)
            print(u)
            
        


studenta = [
    {"name": "Marcel", "score": 75},
    {"name": "David", "score": 45},
    {"name": "Sarah", "score": 85},
    {"name": "Mike", "score": 30},
    {"name": "Grace", "score": 60}
] 

change = Update(studenta)
change.update_score('Marcel', 90)


