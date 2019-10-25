import random

class Student:
    def __init__ (self, name = None, exam_grade = None, partic_grade = None, hw_grade = None, adj1 = None, adj2 = None, adj3 = None, compl_s = None, crit_s = None):
        self.name = name
        self.exam_grade = exam_grade
        self.partic_grade = partic_grade
        self.hw_grade = hw_grade
        self.adj1 = adj1
        self.adj2= adj2
        self.adj3 = adj3
        self.compl_s = compl_s
        self.crit_s = crit_s

def generate_lit_comments(s_name, exam_grade, partic_grade, hw_grade, adj1, adj2, adj3, compl_s = "", crit_s = ""):
    exam_grade_ops = [" has very good exam preparation skills and should keep up the good work.", " has excellent studying habits.", " does very well exams in class.", " may need to improve studying techniques however is still doing fine.", " should put some more effort into studying.", " should focus more on exam preperation."," has a lot of room for improvement with regards to studying for the classes exams.", " struggles with taking tests and should seek outside help.", " fails to do well on exams."]

    partic_grade_ops = [" is also a pleasure to have in my class and always a positive contibutor.", " also is always dilligent in class.", " is always making a positive impact on the class.", " however could improve class participation by coming prepared and having a more positive class impact.", " however is sometimes prone to calling out.", " however can sometimes be disruptive.", " Being disruptive and coming unprepared is a persistant problem that must be fixed.", " Distracting other students is a persiastant problem.", " If bad behaviour continues, further action will be required."]

    hw_grade_ops = ["always completes homework on time and deligently.", " always turns in high quality homework.", " clearly puts a lot of effort into homework.",  " could improve homework habits but usually hands in homework on time.", " could put more effort into doing homework.", " should focus on completing the at home assignments better.", " Late and poor quality homework is unacceptable.", " Completing homework is necessary to do well in my class.", " Late submission and low effort seems to be a persistant problem."]

    sentence = compl_s
    if exam_grade >= 90:
        sentence += " " + s_name + exam_grade_ops[random.randint(0,2)]
    elif 80 <= exam_grade < 90:
         sentence += " " + s_name + exam_grade_ops[random.randint(3,5)]
    else:
        sentence += " " + s_name + exam_grade_ops[random.randint(6,8)]

    if partic_grade >= 90:
        sentence += " " + s_name + partic_grade_ops[random.randint(0,2)]
    elif 80 <= partic_grade < 90:
         sentence += " " + s_name + " is also a pleasure to have in class" + partic_grade_ops[random.randint(3,5)]
    else:
        sentence += " " + s_name + " needs to improve class participation." + partic_grade_ops[random.randint(6,8)]

    if hw_grade >= 90:
        sentence += " " + s_name + hw_grade_ops[random.randint(0,2)]
    elif 80 <= hw_grade < 90:
         sentence += " " + s_name + hw_grade_ops[random.randint(3,5)]
    else:
        sentence += " " + s_name + " needs to do better on homework." + hw_grade_ops[random.randint(6,8)]

    sentence += " Overall, I would say that " + s_name + " is " + adj1 + ", " + adj2 + ", and " + adj3 + ". "
    sentence += crit_s
    return sentence

def main():
    students = []

    stephane = Student("Stephane", 92, 86, 65, "hardworking", "lazy", "excited", "Stephane is always on time to class.", "Stephane could work on not calling out in class.")
    duncan = Student("Duncan", 76, 98, 88, "dilligent", "studious", "tardy", "Duncan always completes work.", "Duncan never shows up to class.")
    students.append(stephane)
    students.append(duncan)

    for student in students:
        comment = generate_lit_comments(student.name, student.exam_grade, student.partic_grade, student.hw_grade, student.adj1, student.adj2, student.adj3, student.compl_s, student.crit_s)
        print (comment)
        print ("\n")

    return comment

main ()